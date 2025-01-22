from obspy import read
st = read("/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/S0001_MC-PH1_0248_20240405_142022.seed")
print(st)
st.plot()
