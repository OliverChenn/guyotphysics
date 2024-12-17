import pandas as pd

def get_catalog_data(fname):
    iter = 1
    maxi = 100000000000000000
    data = 'bogus'
    data_array = []

    with open(fname) as file:
        # https://stackoverflow.com/questions/54839128/filling-an-array-in-python
        # While counter is below maximum and data is not empty
        while iter <= maxi and data:
            data = file.readline().strip()
            if not data:
                break
            # Parse the data and assign it to variable values
            values = data.split()
            x = float(values[0])
            y = float(values[1])
            magnitude = float(values[2])
            # Make a row/column table
            data_array.append((x, y, magnitude))
            iter += 1

    lat = []
    lon = []
    mags = []
    for entry in data_array:
        lat.append(entry[0])
        lon.append(entry[1])
        mags.append(entry[2])

    # Convert lists to pandas Series or you get an "not an iterable argument" error
    # when you work on these entries with other functions, e.g, "max"
    lat_series = pd.Series(lat, name='Latitude')
    lon_series = pd.Series(lon, name='Longitude')
    mags_series = pd.Series(mags, name='Magnitude')

    return lat_series, lon_series, mags_series