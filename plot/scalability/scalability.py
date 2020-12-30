import matplotlib.pyplot as plt

# Measurements from throughput.data

# Measurements from latency.data



def do_plot():
    f, ax = plt.subplots(2,1, figsize=(6,5))
    replicaNo = [4, 8, 16, 32]
    xticks = [0,4, 8, 16, 32, 40]
    xticks_label = ["","4", "8", "16", "32", "64", ""]
    thru = [
    ('HotStuff',[
        [119.2815, 118.939],
        [90.721, 83.114],
        [65.721, 68.168],
        [39.309, 36.254],
#         [21.741, 20.710]
    ], '-o', 'coral'),
    ('2CHS',[
        [119.565, 115.069],
        [108.572, 109.417],
        [80.644, 79.838],
        [49.601, 52.035],
#         [26.917, 27.486]
    ], '-^', 'darkseagreen'),
    ('Streamlet',[
        [122.572, 114.046],
        [114.186, 117.320],
        [66.533, 69.830],
        [40.558, 42.116],
#         [22.331, 23.164]
    ], '-s', 'steelblue')
    ]
    for name, entries, style, color in thru:
        thru = []
        errs = []
        for item in entries:
            thru.append((item[0]+item[1])/2.0)
            errs.append(abs(item[0]-item[1]))
        ax[0].errorbar(replicaNo, thru, yerr=errs, fmt=style, mec=color, color=color, mfc='none', label='%s'%name, markersize=6)
#         ax[0].errorbar(replicaNo, thru, yerr=errs, marker='s', mfc='red', mec='green', ms=20, mew=4)
        ax[0].set_ylabel("Throughput (KTx/s)")
        ax[0].legend(loc='best', fancybox=True,frameon=False,framealpha=0.8)
        ax[0].set_xticks(xticks)
        ax[0].set_ylim([0,140])
        ax[0].set_xticklabels(xticks_label)
        ax[0].set_xticklabels(("", "", "", "", "", ""))
    lat = [
    ('HotStuff',[
        [8.5, 8.8],
        [18.4, 18.9],
        [52.2, 54.5],
        [206, 211],
    ], '-o', 'coral'),
    ('2C-HS',[
        [6.6, 6.7],
        [18.7, 19.1],
        [49.4, 50.5],
        [201, 206],
    ], '-^', 'darkseagreen'),
    ('Streamlet',[
        [6.4, 6.6],
        [18.15, 18.7],
        [47.3, 50.1],
        [193, 197],
    ], '-s', 'steelblue')
    ]
    for name, entries, style, color in lat:
        lat = []
        errs = []
        for item in entries:
            lat.append((item[0]+item[1])/2.0)
            errs.append(abs(item[0]-item[1]))
        ax[1].errorbar(replicaNo, lat, yerr=errs, fmt=style, color=color, mec=color, mfc='none', label='%s' % name, markersize=6)
        ax[1].set_ylabel("Latency (ms)")
        ax[1].set_xticks(replicaNo)
        ax[1].set_xticks(xticks)
        ax[1].set_ylim([0,220])
        ax[1].set_xticklabels(xticks_label)
    ax[0].grid(linestyle='--', alpha=0.3)
    ax[1].grid(linestyle='--', alpha=0.3)
    f.text(0.5, 0.04, 'Number of Nodes', ha='center', va='center')
    plt.subplots_adjust(hspace=0.1)
    plt.savefig('scalability.pdf', format='pdf')
    plt.show()

if __name__ == '__main__':
    do_plot()
