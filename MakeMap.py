from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1

my_map = Basemap(projection='merc', lat_0=40.0583, lon_0=-74.4057,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-75.259, llcrnrlat=41.032,
    urcrnrlon=-73.922, urcrnrlat=40.324)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawstates(color='b')

# HERE YOU SHOULD READ EQDATA INSTEAD

# fghjkl
# These are the coordinates
lat1, lon1 = 40.728, -74.675
lat2, lon2 = 40.716, -74.757
lat3, lon3 = 40.6915, -74.749
lat4, lon4 = 40.6978, -74.7463
lat5, lon5 = 40.690, -74.7665
lat6, lon6 = 40.6963, -74.7596
lat7, lon7 = 40.7125, -74.757

# YOU SHOULD ALSO MAKE A LIST OF COLORS AND SYMBOLS

# THIS YOU SHOULD REFORMULATE AS A LOOP
for xpt, ypt in xpt, ypt((lon1, lat1), (lon7, lat7))

xpt, ypt = my_map(lon1, lat1)
my_map.plot(xpt, ypt, 'bo')

xpt, ypt = my_map(lon2, lat2)
my_map.plot(xpt, ypt, 'ro')

xpt, ypt = my_map(lon3, lat3)
my_map.plot (xpt, ypt, 'go')

xpt, ypt = my_map(lon4, lat4)
my_map.plot (xpt, ypt, 'co')

xpt, ypt = my_map(lon5, lat5)
my_map.plot (xpt, ypt, 'mo')

xpt, ypt = my_map(lon6, lat6)
my_map.plot (xpt, ypt, 'yo')

xpt, ypt, = my_map(lon7, lat7)
my_map.plot (xpt, ypt, 'ko')

# HERE YOU MAKE THE LEGEND

# MAKE THIS A LOOP, BEGIN FROM THE TOP LEFT CORNER AND INCREMENT DOWN BY ONE EVERY ONE OF EARTHQUAKES

x1 = [-74.675]
y1 = [40.728]

x2 = [-74.757]
y2 = [40.716]

x3 = [-74.749]
y3 = [40.6915]

x4 = [-74.7463]
y4 = [40.6978]

x5 = [-74.7665]
y5 = [40.690]

x6 = [-74.7596]
y6 = [40.6963]

x7 = [-74.757]
y7 = [40.7125]

# AGAIN LOOP, AND USE THE THIRD COLUMN OF THE EARTHQUAKE COORDINATES
plt.plot(x1, y1, 'blue', label='2.6')
plt.plot(x2, y2, 'red', label='2.9')
plt.plot(x3, y3, 'green', label='2.6')
plt.plot(x4, y4, 'cyan', label='3.7')
plt.plot(x5, y5, 'magenta', label='2.6')
plt.plot(x6, y6, 'yellow', label='4.8')
plt.plot(x7, y7, 'black', label='2.9')


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

