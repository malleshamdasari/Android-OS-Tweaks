import os
import time
import signal
import subprocess

runs = 20
load = [1, 2, 3, 4]
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4']#, 'output_235K_320_labeled.mp4']
if not os.path.exists('logs'):
    os.makedirs('logs')

for run in range(runs):
	print 'run'+str(run)
	os.system('adb shell rm -rf /sdcard/log.txt')
	for l in load:
		pro = {}
		cmd = 'adb shell /data/local/load.exe'
		print 'Load: '+str(l*25)
		for lo in range(l):
			pro[lo] = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
		for vid in videos:
			res = vid[7:17]
			print res
			os.system('adb shell am start -a com.google.android.exoplayer.demo.action.VIEW -d file:////sdcard/' + vid)
			time.sleep(300)
			os.system('adb shell am force-stop com.google.android.exoplayer2.demo')
			os.system('adb pull /sdcard/log.txt logs/log_'+str(run)+'_'+str(l)+'_'+str(res)+'.txt')
		os.system('killall adb')
		time.sleep(2)
