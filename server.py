import socket
import cv2
import sys
from threading import Thread, Lock
import sys
import numpy as np


localIP= "127.0.0.1"
localPort= 5556
bufferSize= 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
running=True

cap = cv2.VideoCapture('video.mp4')
message, address = UDPServerSocket.recvfrom(bufferSize)
# Listen for incoming datagrams
while(running):
    # message = message.decode('utf-8')
    ret, frame = cap.read()
    if ret == False:
        cap = cv2.VideoCapture('video.mp4')
        ret, frame = cap.read()
    d = frame.flatten()
    n = int(len(d)/bufferSize)
    for i in range(n):
        chunk = d[i*bufferSize:(i+1)*bufferSize]
        UDPServerSocket.sendto(chunk,address)
cap.release()
cv2.destroyAllWindows()