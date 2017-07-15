import os
import time

runs = 20
load = [1, 2, 3, 4]
videos=['output_5800K_1920_labeled.mp4', 'output_3000K_1280_labeled.mp4', 'output_235K_320_labeled.mp4']

for run in range(4, runs):
	for l in load:
		for vid in videos:
			os.system('adb shell am start -a android.intent.action.VIEW  -d file:////sdcard/' + vid)
			time.sleep(300)
			os.system('adb shell am force-stop org.videolan.vlc.debug')
