from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import ReadCatalog  # Custom module for reading data
import matplotlib as mpl
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Read your catalog data (e.g., [[40.74, -74.72, 2.5], [34.05, -118.25, 3.1], ...])
data = ReadCatalog.get_catalog_data()

# Extract latitudes and longitudes to determine boundaries
lats = [row[0] for row in data]
lons = [row[1] for row in data]

# Compute tighter map boundaries with a smaller buffer
buffer = 0.25  # Smaller buffer for tighter zoom
llcrnrlon, llcrnrlat = min(lons) - buffer, min(lats) - buffer  # Lower-left corner
urcrnrlon, urcrnrlat = max(lons) + buffer, max(lats) + buffer  # Upper-right corner

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

for row in data:
    lat, lon, mag = row  # Unpack latitude, longitude, and magnitude
    xpt, ypt = my_map(lon, lat)  # Convert to map projection coordinates
    my_map.plot(xpt, ypt, color=colmap(mag / 5), marker='o', markersize=8)

# Add title and labels
plt.title('Earthquake occurrence across the United States')
plt.xlabel('longitude')
plt.ylabel('latitude')

# Create a ScalarMappable for the colorbar with range 0 to 5
norm = Normalize(vmin=0, vmax=5)
cmappable = ScalarMappable(norm=norm, cmap=colmap)

# Add the colorbar at the bottom of the figure
cbar = fig.colorbar(cmappable, ax=ax, orientation='horizontal', fraction=0.046, pad=0.04)
cbar.set_label('Magnitude')

# Show the plot
plt.show()