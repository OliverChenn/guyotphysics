from obspy import read
st = read("/Users/oliverchen/PyCharmProjects/guyotphysics/DATA/S0001_MC-PH1_0248_20240405_142022.seed")
print(st)
for tr in st:
    data_abs = abs(tr.data)
    max_amp = max(data_abs)
    threshold = max_amp * 0.05

    mask = data_abs > threshold
    start_idx = mask.argmax()
    end_idx = len(mask) - mask[::-1].argmax()

    tr.trim(tr.stats.starttime + start_idx * tr.stats.delta,
            tr.stats.starttime + end_idx * tr.stats.delta)
st.plot(size=(1600, 1200), dpi=200)

# colors = ["red", "green", "blue"]

# for i, tr in enumerate(st):
  #  tr.plot(color=colors[i % len(colors)], linewidth=1.5)

st.plot()
