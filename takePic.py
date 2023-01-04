from time import sleep
from picamera import PiCamera
from PIL import Image
import redis

def take_pic(file_name,cam):
    camera = cam
    camera.resolution = (1024, 768)
    #camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(file_name)
    im = Image.open(file_name) 
    return im
    #r = redis.Redis(host="ip", port=6379)
