import socket
import cv2
import numpy as np
import sys
import time

msgFromClient= "Hello UDP Server"

bytesToSend= str.encode(msgFromClient)

serverAddressPort= ("127.0.0.1", 5556)

bufferSize= 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
running=True
s=[]
n = 6075
while running:
    chunk,address = UDPClientSocket.recvfrom(bufferSize)
    s.extend(chunk)
    
    if (len(s) == (bufferSize*n)):
        f = np.frombuffer(bytes(s),dtype=np.uint8)
        f= f.reshape(1080,1920,3)
        print(f)
        cv2.imshow('Video',f)
        s=[]
        break