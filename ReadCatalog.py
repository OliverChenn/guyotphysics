import pandas as pd


df = pd.read_csv('/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/eqdata1.csv'
)
def make_df(fname):
    df = pd.read_csv(fname)
    lat, lon, magnitude = df['latitude'], df['longitude'], df['mag']
    return lat, lon, magnitude
    print(lat, lon, magnitude)

    return lat, lon, magnitude


