import os
import time
import signal
import subprocess

runs = 20
load = [4]
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4']#, 'output_235K_320_labeled.mp4']
if not os.path.exists('logs'):
    os.makedirs('logs')

for l in load:
	os.system('adb shell rm -rf /sdcard/mallesh.txt')
	os.system('adb shell rm -rf /sdcard/drop.txt')
	pro = {}
	cmd = 'adb shell /data/local/a.out'
	print 'Load: '+str(l*25)
	for lo in range(l):
		pro[lo] = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	for run in range(12, runs):
		print 'run'+str(run)
		for vid in videos:
			res = vid[7:17]
			print res
			os.system('adb shell am start -a android.intent.action.VIEW  -d file:////sdcard/' + vid)
			time.sleep(300)
			os.system('adb shell am force-stop org.videolan.vlc.debug')
			os.system('adb pull /sdcard/mallesh.txt logs/log_'+str(l)+'_'+str(run)+'_'+str(res)+'.txt')
			os.system('adb pull /sdcard/drop.txt logs/drop_'+str(l)+'_'+str(run)+'_'+str(res)+'.txt')
			time.sleep(2)
	os.system('killall adb')
	time.sleep(2)
