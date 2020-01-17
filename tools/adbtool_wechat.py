import os,time
os.system("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI")
time.sleep(0.5)
os.system("adb shell input tap 1009 99")
os.system("adb shell input tap 915 556")