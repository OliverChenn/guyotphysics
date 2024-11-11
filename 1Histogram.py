from ReadCatalog import *
import matplotlib.pyplot as plt

mags = make_df('/Users/oliverchen/PyCharmProjects/guyotphysics/1eqdata')[2]

plt.hist(mags,bins=20,)

plt.title('Histogram of earthquakes')
plt.show()
