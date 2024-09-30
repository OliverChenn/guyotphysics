# Given a file called eqdata, open it, and read its contents
import numpy as np
# This defines the filename
fname='/Users/oliverchen/PyCharmProjects/guyotphysics/eqdata'
# This opens the file


iter = 1
maxi = 100000000000000000
data = 'bogus'

data_array = []


with open(fname) as file:
    while iter <= maxi and data:
        data = file.readline().strip()

        if not data:
            break

        values = data.split()

        if len(values) >= 3:
            x = float(values[0])
            y = float(values[1])
            magnitude = float(values[2])
            data_array.append((x, y, magnitude))

        iter += 1
for entry in data_array:
    # Define the maximum iterations and initialize variables

    print(f"x: {entry[0]}, y: {entry[1]}, Magnitude: {entry[2]}")

