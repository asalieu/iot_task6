from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_recording()
    camera.capture('/home/pi/Desktop/task6/video.h264)
camera.stop_recording()