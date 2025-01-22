#!/usr/bin/env python
import glob
from obspy.core import read
for file in glob.glob('*.z'):
    st = read(file)
    tr = st[0]
    msg = "%s %s %f %f" % (tr.stats.station, str(tr.stats.starttime),
                           tr.data.mean(), tr.data.std())
    print(msg)