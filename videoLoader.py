import socket
import cv2
import sys
from threading import Thread, Lock
import sys
import numpy as np


localIP= "127.0.0.1"
localPort= 5557
bufferSize= 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
running=True

cap = cv2.VideoCapture('video.mp4')

# Listen for incoming datagrams
while(running):

    # message, address = UDPServerSocket.recvfrom(bufferSize)
    # message = message.decode('utf-8')
    ret, frame = cap.read()
    if ret == False:
        cap = cv2.VideoCapture('video.mp4')
        ret, frame = cap.read()
    d = frame.flatten()
    n = int(len(d)/bufferSize)
    s=[]
    for i in range(n):
        chunk = d[i*bufferSize:(i+1)*bufferSize]
        s.extend(chunk)
        if (len(s) == (bufferSize*n)):
            f = np.frombuffer(bytes(s),dtype=np.uint8)
            f=f.reshape(1080,1920,3)
            cv2.imshow('frame',f)
            print(f)
    break
    # cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # UDPServerSocket.sendto(bytesToSend, address)
    # break
cap.release()
cv2.destroyAllWindows()