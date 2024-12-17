import pandas as pd
# Defines a function
def make_df(fname):
    # Reads the csv file
    df = pd.read_csv(fname)
    # Extracts various values - get out the time also
    lat, lon, magnitude = df['latitude'], df['longitude'], df['mag']

    return lat, lon, magnitude
