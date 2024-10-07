from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import ReadCatalog
import numpy as np
import pandas as pd
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
# data = pd.read_csv('./eqdata', delimiter='', header=None,)
data = ReadCatalog.get_catalog_data()

plt.figure(figsize=(10, 10))
my_map = Basemap(projection='merc',
#calculate these things from the data
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


# HERE YOU MAKE THE LEGEND

# MAKE THIS A LOOP, BEGIN FROM THE TOP LEFT CORNER AND INCREMENT DOWN BY ONE EVERY ONE OF EARTHQUAKES
xs = [-74.675, -74.757, -74.749, -74.7463, -74.7665, -74.7596, -74.757]
ys = [40.728, 40.716, 40.6915, 40.6978, 40.690, 40.6963, 40.7125]
x1 = [-74.67]
y1 = [40.728]

# AGAIN LOOP, AND USE THE THIRD COLUMN OF THE EARTHQUAKE COORDINATES
plt.plot(x1, y1, 'blue', label='2.6')


plt.title('Earthquake occurrence between April and May\nin New Jersey ')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend()


# my_map.scatter(x=lon1, y=lat1, latlon=True)
# plt.scatter(x,y=lon1, marker='o', cmap=ts, , 'merc'='plasma', latlon=True)
# plt.scatter(x=lon1, y=lat1, marker='o', color='Blue')
# x,y = my_map(lon, lat)
# my_map.plot(x, y, 'bo', markersize=10)

# 1. figure out class and object in Python (in programming in general)
# 2. ways to call a function and class method in Python (args and kwargs)
# 3. make sure you understand variables and function arguments (why



plt.show()

