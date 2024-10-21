from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import ReadCatalog
import folium
import pandas as pd
import branca.colormap as cm
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as pm
import matplotlib as mpl
# data = pd.read_csv('./eqdata', delimiter='', header=None,)
data = ReadCatalog.get_catalog_data()

plt.figure(figsize=(10, 10))
my_map = Basemap(projection='merc',
# calculate these things from the data
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
    resolution = 'i',
    llcrnrlon=-74.829, llcrnrlat=40.740,
    urcrnrlon=-74.652, urcrnrlat=40.651)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawstates(color='b')

# These are the coordinates
locations =[]
for row in data:
    first_column = row[0]
    second_column = row[1]
    third_column = row[2]
    locations.append([first_column, second_column, third_column])

# YOU SHOULD ALSO MAKE A LIST OF COLORS AND SYMBOLS
colors = ['bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo']
cmap = mpl.colormaps['rainbow']
# THIS YOU SHOULD REFORMULATE AS A LOOP
for i, (lat, lon, mag ) in enumerate(locations):
    xpt, ypt = my_map(lon, lat)
    c=cmap(mag/5)
    print(c)
    my_map.plot(xpt, ypt, color=(0,0,1,mag/5), marker='o')

fig, ax = plt.subplots(figsize=(6, 1))  # Adjust size if needed
fig.subplots_adjust(bottom=0.5)

cb = plt.colorbar(
    pm.ScalarMappable(norm=mcolors.Normalize(vmin=1, vmax=5), cmap=pm.Blues),
    cax=ax, orientation='horizontal'
)




plt.title('Earthquake occurrence between April and May\nin New Jersey ')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()

plt.show()

