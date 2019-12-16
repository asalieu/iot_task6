import os
import glob
from picamera import PiCamera
from time import sleep

#fpath ="C:\\Users\\C#\\demofile.py";

if os.path.isfile("video.h264"):
  os.remove("video.h264")  
else:    
  camera.start_recording()
  camera.capture('/home/pi/Desktop/task6/video.h264)
  camera.stop_recording()
  camera = PiCamera()  
