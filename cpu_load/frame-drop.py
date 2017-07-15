import os
import time

runs = 10
cp_freq = os.popen('adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies').read().strip().split(' ')
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4', 'output_235K_320_labeled.mp4']
#videos = ['output_720x2180.mp4']
cp_freq = cp_freq[2:]
if not os.path.exists('logs'):
    os.makedirs('logs')

def calculate_utilization():
	stat1 = open('stat1.txt', 'r')
	time.sleep(5)
	stat2 = open('stat2.txt', 'r')
	stats = {}
	for line in stat1:
		stats[0] = [int(x) for x in line.split()[1:]]
		break
	for line in stat2:
		stats[1] = [int(x) for x in line.split()[1:]]
		break
	print stats
	total = stats[1][0]+stats[1][1]+stats[1][2] - stats[0][0]-stats[0][1]-stats[0][2]
	return float(total)/60

for run in range(runs):
	os.system('adb shell rm -rf sdcard/mallesh.txt')
	for cp_f in cp_freq:
		print "CP Frequency: "+str(cp_f)
		os.system('adb shell \"echo '+str(cp_f)+' > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq\"')
		os.system('adb shell \"echo '+str(cp_f)+' > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq\"')
		time.sleep(2)
		for vid in videos:
			res = vid[7:17]
			print res
			os.system('adb shell am start -a android.intent.action.VIEW  -d file:////sdcard/' + vid)
			time.sleep(300)
			os.system('adb shell am force-stop org.videolan.vlc.debug')
			os.system('adb pull /sdcard/mallesh.txt logs/log_'+str(run)+str(cp_f)+str(res)+'.txt')
			os.system('adb pull /sdcard/drop.txt logs/drop_'+str(run)+str(cp_f)+str(res)+'.txt')
