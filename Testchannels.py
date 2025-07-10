# Loads 6 channels from a specific day at a specific time

# Written by Oliver Chen

from os import listdir
from obspy import Stream
from obspy import read

#the one specific example
# These are strings
diro= "/Users/oliverchen"
seis= "Seismometer2"
year= "2021"
month= "07"
day= "11"
# This is a number
hour = 3

########################

# Below is one way to concatenate a string
#seeds = listdir(f"{diro}/{seis}/{year}/{month}/{day}")
# Here's another way
prefx= "PP.S0002.00.HHX_centaur-6_2977_"+year+month+day+"_"
prefy= "PP.S0002.00.HHY_centaur-6_2977_"+year+month+day+"_"
prefz= "PP.S0002.00.HHZ_centaur-6_2977_"+year+month+day+"_"
# Next 3 channels
prefnx= "PP.S0002.10.HNX_centaur-6_2977_"+year+month+day+"_"
prefny= "PP.S0002.10.HNY_centaur-6_2977_"+year+month+day+"_"
prefnz= "PP.S0002.10.HNZ_centaur-6_2977_"+year+month+day+"_"

suff= ".miniseed"

# Making a formatted print
# print (f"{hour:02d}0000")
shour = f"{hour:02d}0000"
# Construct a better file name for each of the HH* files
file1= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefx+shour+suff
file2= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefy+shour+suff
file3= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefz+shour+suff
# Construct a better file name for each of the HN* files
file4= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefnx+shour+suff
file5= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefny+shour+suff
file6= diro+"/"+seis+"/"+year+"/"+month+"/"+day+"/"+prefnz+shour+suff

# Work on making the ONE plot here (and then if it works, copy and put into MakeRecord

# open stream
#st1 = Stream()
#st2 = Stream()
st3 = Stream()

#st4 = Stream()
#st5 = Stream()
st6 = Stream()
try:
    try:
      #  st1 += read(file1)
      #  st2 += read(file2)
        st3 += read(file3)
    except:
        print("err1")
        pass
    try:
       # st4 += read(file4)
       # st5 += read(file5)
        st6 += read(file6)
    except:
        print("err2")
        pass

    # A way to use obspy to recognize this as multi channel and plot at the same time
    # The order doesn't matter, it's ordering by the hole number 00 and 10
    # st = st3 + st6
    # st.plot()
except:
    print("err3")
    pass

# TRY TO MEASURE SOMETHING IN YOUR TRACES
# THAT TELLS YOU SOMETHING ABOUT THEM
# THAT YOU CAN ALSO SEE IN YOUR PLOT
# A STATISTIC E G
data = st3[0].data.tolist()
min = min(data)
max = max(data)
range = max - min
mean = sum(data) / len(data)
# variance = how spread out the data is
variance = sum((x - mean) ** 2 for x in data) / len(data)
# std = standard deviation
std = variance ** 0.5

print(min)
print(max)
print(range)
print(mean)
print(variance)
print(std)
