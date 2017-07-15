import numpy as np
import matplotlib.pyplot as plt

f = plt.figure()
def cdf(data, Colour, Label):
    global f
    data_size=len(data)

    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)

    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    # Plot the cdf
    plt.plot(bin_edges[0:-1], cdf,linestyle='--', color=Colour, label=Label)
    plt.ylim((0,1))
    plt.ylabel("CDF")
    plt.xlabel("Presentation Delay (ms)")
    plt.legend(loc='lower right')
    #f.savefig("cdf-late.pdf")

a = np.loadtxt('late-fullhd-vlc.txt')
b = np.loadtxt('late-hd-vlc.txt')
c = np.loadtxt('late-vga-vlc.txt')
d = np.loadtxt('late-fullhd-exo.txt')
e = np.loadtxt('late-hd-exo.txt')
f = np.loadtxt('late-vga-exo.txt')
cdf(a, 'r', 'FullHD VLC')
cdf(b, 'g', 'HD VLC')
cdf(c, 'b', 'VGA VLC')
cdf(d, 'y', 'FullHD Exo')
cdf(e, 'm', 'HD Exo')
cdf(f, 'c', 'VGA Exo')
plt.show()
