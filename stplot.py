from obspy import read
import matplotlib.pyplot as plt

# Made a loop so I don't copypaste 50 miniseeds
file_list_path = "/Users/oliverchen/Seismometer2/top50"

with open(file_list_path, "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue  # skip empty lines

    # Extract only the filepath (first token)
    filepath = line.split()[0]

    filename = filepath.split('/')[-1]

    # Extract component from filename (4th dot-separated part, before underscore)
    try:
        component = filename.split('.')[3].split('_')[0]
    except IndexError:
        print(f"Skipping line (can't parse component): {line}")
        continue

    group1 = ["HHX", "HHY", "HHZ"]
    group2 = ["HNX", "HNY", "HNZ"]

    if component in group1:
        components = group1
    elif component in group2:
        components = group2
    else:
        print(f"Skipping line (unknown component): {line}")
        continue

    # Get other two components in the same group
    other_cmp = [c for c in components if c != component]

    # Build paths for other components by replacing component string in filepath
    prefix = filepath[:filepath.index(component)]
    suffix = filepath[filepath.index(component) + len(component):]

    path1 = filepath
    path2 = prefix + other_cmp[0] + suffix
    path3 = prefix + other_cmp[1] + suffix

    paths = [path1, path2, path3]

    traces = []
    for path in paths:
        try:
            st = read(path)
            st.detrend("demean")
            traces.append(st[0])
        except FileNotFoundError:
            print(f"File not found: {path}")

    if len(traces) == 0:
        print(f"No valid files found for base file: {filepath}")
        continue

    # Plotting all traces stacked vertically
    fig, axes = plt.subplots(len(traces), 1, figsize=(12, 3*len(traces)), sharex=True)

    # If only one trace, axes is not a list, fix that:
    if len(traces) == 1:
        axes = [axes]

    for i, tr in enumerate(traces):
        start = tr.stats.starttime
        end = start + 3600  # 1 hour window
        tr_trimmed = tr.copy().trim(starttime=start, endtime=end)
        times_sec = tr_trimmed.times()

        ax = axes[i]
        ax.plot(times_sec, tr_trimmed.data, label=tr_trimmed.id)
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        ax.legend(loc="upper right")

    axes[-1].set_xlabel("Time (seconds)")
    plt.tight_layout()

    output_file = filepath.replace(".miniseed", ".pdf")
    plt.savefig(output_file)
    plt.close(fig)

    print(f"{output_file}")



