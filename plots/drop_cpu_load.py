import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 6
FullHD_VLC = (0.18, 2.9, 6.8, 19.3, 26.8, 37.5)
HD_VLC = (0, 0.3, 0.28, 2.8, 5.2, 10.8)
VGA_VLC = (0, 0, 0.24, 0.4, 2.8, 6.5)
FullHD_Exo = (0.1, 0.8, 4.2, 12.3, 22, 35.5)
HD_Exo = (0, 0, 0.2, 1.0, 3.1, 8.2)
VGA_Exo = (0, 0, 0, 0.2, 1.7, 5.8)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.8
 
rects1 = plt.bar(index, FullHD_VLC, bar_width,
                 alpha=opacity,
                 color='r',
                 label='FullHD-VLC')
 
rects2 = plt.bar(index + bar_width, FullHD_Exo, bar_width,
                 alpha=opacity,
                 color='b',
                 label='FUllHD-Exo')

rects3 = plt.bar(index+ 2*bar_width, HD_VLC, bar_width,
                 alpha=opacity,
                 color='g',
                 label='HD-VLC')
 
rects4 = plt.bar(index + 3*bar_width, HD_Exo, bar_width,
                 alpha=opacity,
                 color='m',
                 label='HD-Exo')
 
rects5 = plt.bar(index+ 4*bar_width, VGA_VLC, bar_width,
                 alpha=opacity,
                 color='c',
                 label='VGA-VLC')
 
rects6 = plt.bar(index + 5*bar_width, VGA_Exo, bar_width,
                 alpha=opacity,
                 color='y',
                 label='VGA-Exo')
 
plt.xlabel('CPU Load (%)', fontsize=16)
plt.ylabel('Frame Drop Ratio (%)', fontsize=16)
plt.xticks(index + bar_width, (0, 20, 40, 60, 80, 100), fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.savefig('frameDrop.pdf') 
#plt.tight_layout()
plt.show()
