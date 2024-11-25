import pandas as pd
#defines a function
def make_df(fname):
    #reads the csv file
    df = pd.read_csv(fname)
    #calls on these 3 values
    lat, lon, magnitude = df['latitude'], df['longitude'], df['mag']

    return lat, lon, magnitude


