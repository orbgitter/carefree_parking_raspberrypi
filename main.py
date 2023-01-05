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
import mongo
import pymongo

def main():
      name='pic.jpg'
      name2='pi.png'
      print('start server')
      gate=barrier.Barrier()
      r = redis.Redis(host="", port=6379)#ip=3.112.247.246
      my_mongo_client = pymongo.MongoClient("mongodb://54.173.237.181:27017/")
      r.set('ans','False')
      while(True):
            im=takePic.take_pic(name)#update with redis
            with open(name,"rb") as imageFile:
                  
                  str=base64.b64encode(imageFile.read())
                  print(str)
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
                  mongo.set_parking(my_mongo_client)
                  time.sleep(7)
                  while(parking.parking_len()<100.0):
                        time.sleep(2)
                  r.set('parking','no')
                  mongo.set_unparking(my_mongo_client)
                  time.sleep(5)
                  gate.close_barrier()
                  r.set('ans','false')
                  time.sleep(5)
main()
