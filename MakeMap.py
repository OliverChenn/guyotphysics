import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from ReadCatalog import *
from ReadCatalog0 import *
import numpy as np

# set a flag
flag = 1

if flag == 0:
  # Simple space delimited ASCII file for which you use ReadCatalog0
  # Read your catalog data (e.g., [[40.74, -74.72, 2.5], [34.05, -118.25, 3.1], ...])
  fname = '/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata0.csv'
  lats, lons, mags = get_catalog_data(fname)

elif flag == 1:
  # Actual comma-separated-value (csv) file with an actual header for which you use ReadCatalog
  # Get latitudes and longitudes from read catalog to determine boundaries
  fname = '/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata1.csv'
  # Also get out the time
  lats, lons, mags = make_df(fname)

# Between flag 0 and flag 1 the variables lats,lons,mags are of a different type
# and the code that follows understands the second type but not the first
# print(f"{lons}")

# Proceed with the analysis
mmin= min(mags)
mmax= max(mags)
# Get out the time limits
# ftime =
# ltime =

# Make tighter map boundaries with a smaller buffer
buffer = 0.60
rlon=max(lons)-min(lons)
print(f"{max(lons)}")
# These need to be right before moving on
print(f"{min(lons)}")
rlat=max(lats)-min(lats)
# print(f"{min(lons)} {min(lats)} {max(lons)} {max(lats)}")
# print(f"{rlon} {rlat}")
print(f"{buffer}")
print(f"{rlat}")
print(f"{rlon}")

# These are the coordinates of the map corners
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
print(f"(lon)")
print(f"(lat)")
# Add title and labels - also include between what time
# Make a string with that information and then use
#plt.title('Earthquake occurrence across the United States')
print(f"(lon)")
#print("% [flag width . (dot) precision] type" % (value or object))
plt.title(print(
    'Earthquake occurrence across the United States between %s and %s',
    (ftime,ltime))
plt.xlabel('longitude')
plt.ylabel('latitude')

# Draw subdivisions too
# Work on map annotations within the actual boundaries
# Labelled where they intersect the left, right, top or bottom of the plot
my_map.drawmeridians(np.arange(llcrnrlon,urcrnrlon,0.05),
                     dashes=[1,0],linewidth=0.1,
                     labels=[True,True,False,True],
                     fontname='Times New Roman',fontsize=12)
my_map.drawparallels(np.arange(llcrnrlat,urcrnrlat,0.05),
                     dashes=[1,0],linewidth=0.1,
                     labels=[True,True,False,True],
                     fontname='Times New Roman',fontsize=12)

# Create a ScalarMappable for the colorbar with range 0 to 5
norm = Normalize(vmin=mmin, vmax=mmax)
cmappable = ScalarMappable(norm=norm, cmap=colmap)

# Add the colorbar at the bottom of the figure
cbar = fig.colorbar(cmappable, ax=ax, orientation='horizontal', fraction=0.08, pad=0.04)
cbar.set_label('Magnitude')

# Show the plot
plt.show()