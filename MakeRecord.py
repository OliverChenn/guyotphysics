from obspy import read
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from obspy import Stream


# This is reading a file that has combined 6 channels that are called HHX HHY HHZ, HNX HNY HNZ, which are the 3 components each of the velocity sensor and the accelorameter
#st = read("/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/S0002_centaur-6_2977_20250102_010718.seed")
# Load 1 hour each of data, files are stored individually, here is ONE example that works
# st1 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHZ_centaur-6_2977_20220307_110000.miniseed")
# st2 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHX_centaur-6_2977_20220307_110000.miniseed")
# st3 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHY_centaur-6_2977_20220307_110000.miniseed")
# st4 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNZ_centaur-6_2977_20220307_110000.miniseed")
# st5 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNX_centaur-6_2977_20220307_110000.miniseed")
# st6 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNY_centaur-6_2977_20220307_110000.miniseed")


# Improved version, also used for loop
file_paths = [
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHZ_centaur-6_2977_20220307_110000.miniseed",
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHX_centaur-6_2977_20220307_110000.miniseed",
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHY_centaur-6_2977_20220307_110000.miniseed",
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNZ_centaur-6_2977_20220307_110000.miniseed",
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNX_centaur-6_2977_20220307_110000.miniseed",
    "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNY_centaur-6_2977_20220307_110000.miniseed",
]


# Next: write a loop that goes over ALL the files in a directory, ultimately covering ALL your files
# Next: build in a failsafe - what if the file cannot be read, maybe by making an empty one in its place

# Maybe now you can create a big st and append all of the st1, st... to it
# st= # start a "stream" object
# st.append(st1)
# The above didn't work, here's what chatgpt suggested
# st = st1 + st2 + st3 + st4 + st5 + st6

# Makes a empty steam object, allows us to safely append files without breaking the code
st = Stream()
# Loop for failsafe
for file in file_paths:
    try:
        st += read(file)
    except Exception as e:
        print(f"Could not read file")
        st += Stream()

# This code is if all files didn't exist or failed to load. It would raise a error to prevent the code from continuing
if len(st) == 0:
    raise ValueError("No valid MiniSEED files found or loaded")




# Make these file names by taking in the data in by the hour and supplying it by making a string that changes the hour or file name.
# Visually cluttered

#st.decimate(factor=2)

# Defines time window
start_time = st[0].stats.starttime
end_time = start_time + 3600

# Collecting the time series between the times of interest
st_segment = st.slice(starttime=start_time, endtime=end_time)
# Plot the segment - find out how to SET the y-axis limits
fig = st_segment.plot(
    type="relative",
    number_of_ticks=10,
    handle=False,
    title="(beginning)  -----------------------  (end)",
    size=(2000, 1500),
    dpi=200,
    fontsize=100,
    color=('r')
)

# This is for matplotlib usage, still unrefined
# fig, axes = plt.subplots(nrows=len(st), sharex=True)
# for tr, ax in zip(st, axes):
#      times = tr.times('matplotlib')
#      ax.plot(times, tr.data)
# ax.xaxis_date()
# fig.autofmt_xdate()
# plt.subplots_adjust(hspace=0)
# ax.set_ylim(-100000, 100000)
#
# plt.show()
# colors = ['blue', 'blue', 'blue', 'red', 'red', 'red']
# for i, line in enumerate(ax.lines):
#     line.set_color(colors[i])
# ax.set_xlabel("Time (s)", fontsize=14)   # X-axis label
# ax.set_ylabel("Amplitude", fontsize=14)  # Y-axis label
# ax.set_title("Seismic Data", fontsize=16)  # Title
# fig.show()

