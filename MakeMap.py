import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from ReadCatalog import *

fname = '/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata1.csv'
# Read your catalog data (e.g., [[40.74, -74.72, 2.5], [34.05, -118.25, 3.1], ...])
data = make_df(fname)
# Get latitudes and longitudes from read catalogto determine boundaries
lats, lons, mags = make_df(fname)
mmin= min(mags)
mmax= max(mags)
# Make tighter map boundaries with a smaller buffer
buffer = 0.60
rlon=max(lons)-min(lons)
rlat=max(lats)-min(lats)
# print(f"{min(lons)} {min(lats)} {max(lons)} {max(lats)}")
# print(f"{rlon} {rlat}")

llcrnrlon, llcrnrlat = (min(lons) - buffer*(rlon),
                        min(lats) - buffer*(rlat))
urcrnrlon, urcrnrlat = (max(lons) + buffer*(rlon),
                        max(lats) + buffer*(rlat))
# print(f"{llcrnrlon} {llcrnrlat} {urcrnrlon} {urcrnrlat}")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Create the map with dynamic and zoomed-in boundaries
my_map = Basemap(
    projection='merc',
    resolution='i',
    llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat,
    urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat,
    ax=ax
)

# Draw map elements
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawstates(color='b')

# Prepare the colormap and plot points
colmap = mpl.colormaps['rainbow']

# Plots data and makes the color for the points.
for i in range(len(lats)):
    lat, lon, mag = lats[i], lons[i], mags[i]
    xpt, ypt = my_map(lon, lat)
# Scaled between zero and one
    index=(mag-mmin)/(mmax-mmin)
    my_map.plot(xpt, ypt, color=colmap(index), marker='o', markersize=8)

# Add title and labels
plt.title('Earthquake occurrence across the United States')
plt.xlabel('longitude')
plt.ylabel('latitude')

# Create a ScalarMappable for the colorbar with range 0 to 5
norm = Normalize(vmin=mmin, vmax=mmax)
cmappable = ScalarMappable(norm=norm, cmap=colmap)

# Add the colorbar at the bottom of the figure
cbar = fig.colorbar(cmappable, ax=ax, orientation='horizontal', fraction=0.08, pad=0.04)
cbar.set_label('Magnitude')

# Show the plot
plt.show()