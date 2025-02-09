from obspy import read
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st = read("/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/S0002_centaur-6_2977_20250102_010718.seed")



st.decimate(factor=2)
start_time = st[0].stats.starttime
end_time = start_time + 600

st_segment = st.slice(starttime=start_time, endtime=end_time)

st_segment.plot(
    type="relative",
    number_of_ticks=0,
    handle=True,
    title="(beginning)  -----------------------  (end)"
)
st.plot(size=(2000, 1500), dpi=125)




