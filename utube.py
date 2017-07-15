import subprocess
import thread
import os
import sys
import time
from time import gmtime,strftime, sleep
import signal

try:
    viewclient_home = os.environ['ANDROID_VIEW_CLIENT_DIR']
    sys.path.append(os.path.join(viewclient_home,'src'))
except:
    raise

from com.dtmilano.android.viewclient import ViewClient, View

package = 'com.hecorat.screenrecorder.free'
activity = '.activities.MainActivity'
component = package + '/' + activity
device, serialno = ViewClient.connectToDeviceOrExit(serialno='0094d3075388ceb1')
FLAG_ACTIVITY_NEW_TASK = 0x10000000
device.startActivity(component=component, flags = FLAG_ACTIVITY_NEW_TASK)
vc = ViewClient(device=device, serialno=serialno,startviewserver=True)
device.drag((100, 0), (100, 1500), 1000)
vc.dump()
view = vc.findViewById('com.hecorat.screenrecorder.free:id/btn_record')
view.touch()
ViewClient.sleep(2)

os.system('adb shell am start -a android.intent.action.VIEW \"http://www.youtube.com/watch?v=YRhFSWz_J3I\"')
sleep(2)
subprocess.call('adb shell am force-stop com.hecorat.screenrecorder.free',shell=True)
os.system('adb shell am force-stop android.intent.action.VIEW \"http://www.youtube.com/watch?v=YRhFSWz_J3I\"')
