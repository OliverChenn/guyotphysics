# This makes a ...
#
# Written by
from ReadCatalog import *
import matplotlib.pyplot as plt

mags = make_df('/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata1.csv')[2]

plt.hist(mags,bins=20,)

plt.title('Histogram of earthquakes')
plt.show()
