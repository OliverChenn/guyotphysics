from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import ReadCatalog
import numpy as np
import pandas as pd

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
    locations.append([first_column, second_column])

# YOU SHOULD ALSO MAKE A LIST OF COLORS AND SYMBOLS
colors = ['bo', 'ro', 'go', 'co', 'mo', 'yo', 'ko']
# THIS YOU SHOULD REFORMULATE AS A LOOP
for i, (lat, lon ) in enumerate(locations):
    xpt, ypt = my_map(lon, lat)
    my_map.plot(xpt, ypt, colors[i])

    print('i')

plt.title('Earthquake occurrence between April and May\nin New Jersey ')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()

plt.show()

