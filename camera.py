from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
for i in range(2):
    sleep(10)
    camera.capture('/home/pi/Desktop/task6/image%s.jpg'% i)
camera.stop_preview()