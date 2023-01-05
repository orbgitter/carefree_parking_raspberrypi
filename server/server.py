# echo-server.py

import licenceplateML
import redis
from PIL import Image
import myPlates
import base64
#import savePic
#import myPlates
def server():
    print("test")
    name="pic.jpg"
    r=redis.Redis(host="54.173.237.181", port=6379)
    plates=[]
    number=''
    while(True):
        try:
        #r = redis.Redis()
            im=r.get('pic')
            im=im.decode('utf-8')
            im=base64.b64decode(im)
            fh = open(name, "wb")
            fh.write(im)
            fh.close()

            try:
                plates=myPlates.get_plates()
            except Exception as e:
                print("failed to get num")
                print(e)
            number=licenceplateML.getNumber(name)
            if(number!="" and number in plates):
                r.set('ans', 'True')
        except Exception as e:
            print("error in server:")
            print(e)
        """
        im=r.get('pic')
        fh = open(name, "wb")
        fh.write(im.decode('base64'))
        fh.close()
        #im = im.save(name)
        """     
                
    pass

server()




"""
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

            """
