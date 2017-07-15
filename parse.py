import os
import numpy as np
import matplotlib.pyplot as plt

runs = 1
cp_freq = os.popen('adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies').read().strip().split(' ')
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4', 'output_235K_320_labeled.mp4']
cp_freq = cp_freq[2:]

#videos = ['output_720x2180.mp4']
stats = {}
for vid in videos:
    stats[vid[7:17]] = {}

for run in range(runs):
    for cp_f in cp_freq:
        for vid in videos:
            res = vid[7:17]
            lines = open('logs/log_'+str(run)+str(cp_f)+str(res)+'.txt')
            lframes = 0
            dropframes = 0
            nodecodeframes = 0
            futurlateframes = 0
            tframes = 0
            for line in lines:
                line = line.strip().split(':')
                if line[0] == 'noDecodeFrames':
                    nodecodeframes += int(line[1])
                if line[0] == 'lateFrames':
                    lframes += int(line[1])
                    print res, lframes
                if line[0] == 'pLateFrames':
                    futurlateframes += int(line[1])
                if line[0] == 'dropFrames':
                    dropframes += int(line[1])
                if line[0] == 'totalFrames':
                    tframes += int(line[1])
            #if tframes is not 0:
            #stats[res].setdefault(int(cp_f), []).append(float(tframes)/(5*60))
            stats[res].setdefault(int(cp_f), []).append(float(lframes))

for cp_f in cp_freq:
    for vid in videos:
        res = vid[7:17]
	#print res, stats[res][int(cp_f)]
        stats[res][int(cp_f)] = np.mean(stats[res][int(cp_f)])



#plt.title('Frequency vs Frame Drop')
plt.grid(True)
colors=['r','g','b','y','c']

print stats
c = 0
for vid in videos:
    res = vid[7:17]
    lists = sorted(stats[res].items())
    #print lists
    x, y = zip(*lists)
    plt.plot(x, y, '-o', color=colors[c])
    c += 1

p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc=colors[0])
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc=colors[1])
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc=colors[2])
plt.legend((p1, p2, p3), ('5800K X 1920', '1790K X 720','235K X 320'), loc='best')

plt.xlabel('CPU Frequency')
plt.ylabel('Frame Rate')
plt.savefig('frameRate.pdf')
plt.show()
