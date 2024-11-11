import numpy as np
import pandas as pd

fname='/Users/oliverchen/PyCharmProjects/guyotphysics/1eqdata'
df = pd.read_csv('1eqdata')



def make_df(fname):
    df = pd.read_csv(fname)
    lat, lon, magnitude = df['latitude'], df['longitude'], df['mag']
    return lat, lon, magnitude
    print(lat, lon, magnitude)


    return lat, lon, magnitude




# Given a file called eqdata, open it, and read its contents
import numpy as np
# This defines the filename
# def get_catalog_data():
#     fname='/Users/oliverchen/PyCharmProjects/guyotphysics/1eqdata'
#
#     iter = 1
#     maxi = 100000000000000000
#     data = 'bogus'
#
#     data_array = []

    # with open(fname) as file:
    #     # https://stackoverflow.com/questions/54839128/filling-an-array-in-python
    #     # While counter is below maximum and data is not empty
    #     while iter <= maxi and data:
    #         data = file.readline().strip()
    #         # If the data variable is empty
    #         if not data:
    #             break
    #         # Parse the data and assigns it to variable value
    #         values = data.split()
    #         x = float(values[2])
    #         y = float(values[1])
    #         magnitude = float(values[4])
    #         # Make a row/column table
    #         data_array.append((x, y, magnitude))
    #         # this updates the counter
    #         iter += 1
    # # Repeat the table
    #for entry in data_array:
       # print(f"x: {entry[0]}, y: {entry[1]}, Magnitude: {entry[2]}")

