# This makes a histogram of earthquake events from a file

# Written by Oliver Chen
from ReadCatalog import *
import matplotlib.pyplot as plt

mags = make_df('/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata1.csv')[2]

plt.hist(mags,bins=20,)

plt.title('Histogram of earthquakes')
plt.show()
