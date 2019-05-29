from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1280, 720)

camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/IntelligenceVision/Deployimage.jpg')
camera.stop_preview()