# Makes a file that contains statistical records from earthquake loop

# Written By Oliver Chen


from obspy import read
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from obspy import Stream
from os import listdir
import re

flag = 0


# This is reading a file that has combined 6 channels that are called HHX HHY HHZ, HNX HNY HNZ, which are the 3 components each of the velocity sensor and the accelorameter
# st = read("/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/S0002_centaur-6_2977_20250102_010718.seed")
# st.plot()

# Load 1 hour each of data, files are stored individually, here is ONE example that works
# st1 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHZ_centaur-6_2977_20220307_110000.miniseed")
# st2 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHX_centaur-6_2977_20220307_110000.miniseed")
# st3 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHY_centaur-6_2977_20220307_110000.miniseed")
# st4 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNZ_centaur-6_2977_20220307_110000.miniseed")
# st5 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNX_centaur-6_2977_20220307_110000.miniseed")
# st6 = read("/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNY_centaur-6_2977_20220307_110000.miniseed")


# # Improved version, also used for loop
# file_paths = [
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHZ_centaur-6_2977_20220307_110000.miniseed",
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHX_centaur-6_2977_20220307_110000.miniseed",
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.00.HHY_centaur-6_2977_20220307_110000.miniseed",
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNZ_centaur-6_2977_20220307_110000.miniseed",
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNX_centaur-6_2977_20220307_110000.miniseed",
#     "/Users/oliverchen/Seismometer1/2022/03/07/PP.S0002.10.HNY_centaur-6_2977_20220307_110000.miniseed",
# ]

# Using regular expression
# Write a little code that identifies triples of files that correspond to each hour, and have three components
def match_vector_entries(vector, pattern):
    """
    Matches entries in a vector against a regex pattern.

    Args:
        vector: A list of strings.
        pattern: The regex pattern to match.

    Returns:
        A list of strings that match the pattern.
    """
    return [entry for entry in vector if re.search(pattern, entry)]

def DataStats(fname,data,fid):
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    mean_val = sum(data) / len(data)
    # variance = how spread out the data is
    variance_val = sum((x - mean_val) ** 2 for x in data) / len(data)
    # std = standard deviation
    std_val = variance_val ** 0.5
    # Make this a one-liner that uses FORMATTING to give reasonable rounding
    # The 2f means to round to 2 decimals

    # I used the define feature to define the table, then I used print(f") to make a string and the <15 is the spaces and alignment
    def print_statistics_table():
        # Prints info to screen
        print(f"{'Statistic':<20} {'Value':>15}")
        print("-" * 40)
        print(f"{'File Name':<20} {fname:>s}")
        print(f"{'Minimum (Min)':<20} {min_val:>15.2f}")
        print(f"{'Maximum (Max)':<20} {max_val:>15.2f}")
        print(f"{'Range':<20} {range_val:>15.2f}")
        print(f"{'Mean':<20} {mean_val:>15.2f}")
        print(f"{'Variance':<20} {variance_val:>15.2f}")
        print(f"{'Std Deviation':<20} {std_val:>15.2f}")
        # Now also you will print to an existing file
        # print to the fid whichever things you tell it
        # one line, formatted, aligned, YYYY MM DD HH HN min max range mean var std
        fid.write(f"{fname:<15}"+f"{min_val:15.2f}"+f" "+f"{max_val:15.3f}"+f"{range_val:15.2f}"+f"{mean_val:15.2f}"+f"{variance_val:15.2f}"+f"{std_val:15.2f}"+f"\n")
    print_statistics_table()


record_count = 0
# st = Stream()
# # Loop for failsafe
# for file in file_paths
#     try:
#         st += read(file)
#     except Exception as e:
#         print(f"Could not read file")
#         st += Stream()

diro= "/Users/oliverchen"

files = listdir(diro)

hours = range(24)
# Next: write a loop that goes over ALL the files in a directory, ultimately covering ALL your files
# Next: build in a failsafe - what if the file cannot be read, maybe by making an empty one in its place
seiss=match_vector_entries(files, r"^Seismometer\d$")

for seis in seiss:

    # Open a file for sequential write input
    with open(f"{diro}/{seis}/statsfile", "w") as fid:

        years = listdir(f"{diro}/{seis}/")
        # print(f"{years}")
        for year in years:
            months = listdir(f"{diro}/{seis}/{year}")
            # print(f"{months}")
            for month in months:
                if month[0] == '.':
                    continue
                days = listdir(f"{diro}/{seis}/{year}/{month}")
                for day in days:
                    if day[0] == '.':
                        continue
                    for hour in hours:
                        # Below is one way to concatenate a string
                        # seeds = listdir(f"{diro}/{seis}/{year}/{month}/{day}")
                        # Here's another way
                        prefx = "PP.S0002.00.HHX_centaur-6_2977_" + year + month + day + "_"
                        prefy = "PP.S0002.00.HHY_centaur-6_2977_" + year + month + day + "_"
                        prefz = "PP.S0002.00.HHZ_centaur-6_2977_" + year + month + day + "_"
                        # Next 3 channels
                        prefnx = "PP.S0002.10.HNX_centaur-6_2977_" + year + month + day + "_"
                        prefny = "PP.S0002.10.HNY_centaur-6_2977_" + year + month + day + "_"
                        prefnz = "PP.S0002.10.HNZ_centaur-6_2977_" + year + month + day + "_"
                        suff= ".miniseed"
                        shour = f"{hour:02d}0000"

                        file1 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefx + shour + suff
                        file2 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefy + shour + suff
                        file3 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefz + shour + suff
                        # Construct a better file name for each of the HN* files
                        file4 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefnx + shour + suff
                        file5 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefny + shour + suff
                        file6 = diro + "/" + seis + "/" + year + "/" + month + "/" + day + "/" + prefnz + shour + suff
                        # List of MiniSEED files you want to process
                        miniseed_files = [file1, file2, file3, file4, file5, file6]

                        # open stream
                        st1 = Stream()
                        st2 = Stream()
                        st3 = Stream()

                        st4 = Stream()
                        st5 = Stream()
                        st6 = Stream()
                        try:
                            st1 += read(file1)
                            st2 += read(file2)
                            st3 += read(file3)
                        except:
                            print("err1")
                            pass
                        try:
                            st4 += read(file4)
                            st5 += read(file5)
                            st6 += read(file6)
                        except:
                            print("err2")
                            pass

                        st1.detrend("demean")
                        st2.detrend("demean")
                        st3.detrend("demean")
                        st4.detrend("demean")
                        st5.detrend("demean")
                        st6.detrend("demean")

                        # Combine
                        st = st1 + st2 + st3 + st4 + st5 + st6

                        if flag == 1:
                            st.plot(
                                type="relative",
                                number_of_ticks=10,
                                handle=False,
                                title="First 3 Channels",
                                size=(2000, 1500),
                                dpi=200,
                                color='b'
                                # X labels and Y labels needed (it's impossible to do it on a st.plot code)
                            )
                        # Trying to annotate
                        #plt.text(0.5, 0.5, "Start", fontsize=12, color='red')

                        # Write a little other function that takes an input sequence and computes all the below statistics

                        # Call the function that computes all the statistics
                        DataStats(file1, st[0].data.tolist(),fid)
                        DataStats(file2, st[1].data.tolist(),fid)
                        DataStats(file3, st[2].data.tolist(),fid)
                        DataStats(file4, st[3].data.tolist(),fid)
                        DataStats(file5, st[4].data.tolist(),fid)
                        DataStats(file6, st[5].data.tolist(),fid)

                        record_count += 6

                        print(f"\n📦 Total records processed: {record_count}")




