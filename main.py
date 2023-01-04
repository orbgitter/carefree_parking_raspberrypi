import takePic
import client
#import blink
#import licenceplateML
import barrier
import time
import redis
import parking
import io
#import StringIO
import base64
from picamera import PiCamera

def main():
      name='pic.jpg'
      name2='pi.png'
      print('start server')
      camera = PiCamera()
      gate=barrier.Barrier()
      r = redis.Redis(host="", port=6379)
      while(True):
            try:
                  im=takePic.take_pic(name,camera)#update with redis
            except:
                  print('camera buzy')
            with open(name,"rb") as imageFile:
                  
                  str=base64.b64encode(imageFile.read())
                  #print(str)
                  r.set('pic',str)
                  print('seted pic')
                  #a=r.get('pic')
            """
            output = io.StringIO()
            #im = Image.open(name2)
            #im=takePic.take_pic(name)
            with open(name,"rb") as im:
                  im.save(output, format=im.format)

                  #r = redis.StrictRedis(host='localhost')
                  r.set('imagedata', output.getvalue())
                  print('seted pic2')
                  output.close()
                  
            """
            if(r.get('ans').decode('ascii')=="True"):
                  
                  
                  gate.open_barrier()
                  while(parking.parking_len()>100.0):
                        time.sleep(2)
                  r.set('parking','yes')
                  time.sleep(7)
                  while(parking.parking_len()<100.0):
                        time.sleep(2)
                  r.set('parking','no')
                  time.sleep(5)
                  gate.close_barrier()
                  r.set('ans','false')
                  time.sleep(5)
main()
