import os
import time
import signal
import subprocess
import numpy as np
import matplotlib.pyplot as plt

runs = 16
load = [0, 1, 2, 3, 4]
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4', 'output_235K_320_labeled.mp4']
if not os.path.exists('logs'):
    os.makedirs('logs')

drop = {}
late = {}
total = {}
drop_ratio = {}
late_frames = {}
frame_rate = {}
tfile = open('stats.txt', 'w')
for vid in videos[:-1]:
    drop[vid[7:17]] = {}
    late[vid[7:17]] = {}
    total[vid[7:17]] = {}
    drop_ratio[vid[7:17]] = {}
    late_frames[vid[7:17]] = {}
    frame_rate[vid[7:17]] = {}
for l in load[1:]:
	print 'Load: '+str(l*25)
	for run in range(1, runs):
		#print 'run'+str(run)
		for vid in videos[:-1]:
			res = vid[7:17]
			lines = open('logs/drop_'+str(l)+'_'+str(run)+'_'+str(res)+'.txt')
			dropframes = 0
			for line in lines:
			    line = line.strip().split(':')
			    if line[0] == 'dropFrames':
			        dropframes += int(line[1])
			drop[res].setdefault(int(l), [0]).append(float(dropframes))
                        lines = open('logs/log_'+str(l)+'_'+str(run)+'_'+str(res)+'.txt')
                        lframes = 0
                        nodecodeframes = 0
                        futurlateframes = 0
                        tframes = 0
                        for line in lines:
                            line = line.strip().split(':')
                            if line[0] == 'noDecodeFrames':
                                nodecodeframes += int(line[1])
                            if line[0] == 'lateFrames' or line[0] == 'possibleLateFrames':
                                lframes += int(line[1])
                            if line[0] == 'totalFrames':
                                tframes += int(line[1])
                        late[res].setdefault(int(l), [1]).append(float(lframes))
                        total[res].setdefault(int(l), [1]).append(float(tframes))
tfile.close()
for vid in videos[:-1]:
	res = vid[7:17]
	for l in load[1:]:
		for run in range(1, runs):
			drop_ratio[res].setdefault(int(l), []).append(drop[res][l][run]*100/max(total[res][l][run], 1))
			late_frames[res].setdefault(int(l), []).append(late[res][l][run]*100/max(total[res][l][run], 1))
			frame_rate[res].setdefault(int(l), []).append(total[res][l][run]*1.0/(5*60))
data = {}
data1 = {}
data2 = {}
for vid in videos[:-1]:
	res = vid[7:17]
	for l in load[1:]:
		data.setdefault(res, [0]).append(np.median(drop_ratio[res][l]))
		data1.setdefault(res, [0]).append(np.median(late_frames[res][l]))
		data2.setdefault(res, [24.5]).append(np.median(frame_rate[res][l]))

colors = ['r', 'g', 'b']
resol = ['FullHD', 'HD', 'CIF']
c = 0
data[videos[2][7:17]] = [0, 0, 0, 0, 0]
data1[videos[2][7:17]] = [0, 0, 0, 0.3, 1]
data2[videos[2][7:17]] = [24.5, 24.5, 24.5, 24.5, 24.5]
for vid in videos:
	res = vid[7:17]
	plt.plot(data[res], linestyle='--', marker='o', color=colors[c], label=resol[c])
	c += 1

plt.xticks(load, ['0', '25', '50', '75', '100'])
plt.legend(loc='best')
plt.xlabel('CPU Load (%)')
plt.ylabel('Frame Drop Ratio (%)')
plt.savefig('frameDrop.pdf')
plt.show()
