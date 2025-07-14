# Test loop and statistical data

# Written By Oliver Chen

from os import listdir
import re
from obspy import Stream
from obspy import read

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


# How to text match something, quick example
#seis='blbltxtblabla'
#match = re.search(r"txt", seis)
#print(f"{match}")
diro= "/Users/oliverchen"
# Get the directory listing
files = listdir(diro)
#print(f"{files}")
# Within all the elements of file, find the ones that match "Seismometer?", i.e. Seismometer1 and Seismometer2
# This didn't work so I defined the subfunction first
#seis = re.match("Seismometer?", f"{files}")
#print(f"{seis}")
hours = range(24) # Generates numbers between 0 and 23
# This matches a single character followed by the end of the entry
seiss=match_vector_entries(files, r"^Seismometer\d$")
# print(seiss)
for seis in seiss:
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
                    # If next line runs, loop works
                    #print(f"{diro}/{seis}/{year}/{month}/{day}/prefix{hour}suffix")


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

                    # fa way to use obspy to recognize this as multi channel and plot at the same time
                    # The order doesn't matter, it's ordering by the hole number 00 and 10
                    st = st1 + st2 + st3 + st4 + st5 + st6
                    st.plot()

data = st[0].data.tolist()
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
