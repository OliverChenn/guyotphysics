# Plots the 4.8 magnitude earthquake NJ

# Written by Oliver Chen

from obspy import read
import matplotlib.pyplot as plt

# Specify file directory and file name
fdir= "/Users/oliverchen/PycharmProjects/guyotphysics/DATA/"
fnam = "S0002_centaur-6_2977_20240405_142022.seed"
ffname = f"{fdir}{fnam}"

# Read and display data
st1 = read(ffname)
# Try to find the attributes of this new object
# print(st1)
# print(dir(st1))
# Split the seed into miniseed


# Takes 3 traces
traces = st1[:3]

# Create a figure with 3 subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

# Turns it into a collection that you can loop over
#trace = [st1]

# Plots 3 traces
for i, tr in enumerate(traces):
    times = tr.times()
    data = tr.data
    axes[i].plot(times, data, label=tr.id)
    axes[i].set_ylabel("Amplitude")
    axes[i].grid(True)
    # plt.show()
# Make a suitable file name for the output figure
output_file = ffname.replace(".seed",".pdf")
#print(output_file)
plt.savefig(output_file)
# This will plot it
# st1.plot()
#
# # Now loop over the collection
# for i, tr in enumerate(trace):
#     start = tr.stats.starttime
#     end = start + 3600  # 1 hour window
#     tr_trimmed = tr.copy().trim(starttime=start, endtime=end)
#     times_sec = tr_trimmed.times()
#
#     ax = axes[i]
#     ax.plot(times_sec, tr_trimmed.data, label=tr_trimmed.id)
#     ax.set_ylabel("Amplitude")
#     ax.grid(True)
#     ax.legend(loc="upper right")
#
# axes[-1].set_xlabel("Time (seconds)")
# plt.tight_layout()
#
# output_file = filepath.replace(".miniseed", ".pdf")
# plt.savefig(output_file)
# plt.close(fig)
#
# print(f"{output_file}")


