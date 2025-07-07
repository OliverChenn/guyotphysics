# Plots csv file for MakeMap

# Written By Oliver Chen
import pandas as pd
# Defines a function
def make_df(fname):
    # Reads the csv file
    df = pd.read_csv(fname)
    # Extracts various values - get out the time also
    lat, lon, magnitude, time = df['latitude'], df['longitude'], df['mag'], df['time']

    return lat, lon, magnitude, time