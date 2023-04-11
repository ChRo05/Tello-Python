#!/usr/bin/env python

import socket
import time

#Create a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1' , 8889)

#command-mode : 'command'
socket.sendto('command'.encode('utf-8'),tello_address)
print ('start')

# 離陸
socket.sendto('takeoff'.encode('utf-8'),tello_address)
print ('takeoff')

# 180cm上昇
socket.sendto('up 180'.encode('utf-8'),tello_address)
print ('takeoff')
time.sleep(3)

# socket.sendto('left 50'.encode('utf-8'),tello_address)
# time.sleep(3)

# 500cm前進
socket.sendto('forward 500'.encode('utf-8'),tello_address)
time.sleep(3)

# 反時計回り90度
socket.sendto('ccw 90'.encode('utf-8'),tello_address)
time.sleep(3)

# 500cm前進
socket.sendto('forward 500'.encode('utf-8'),tello_address)
time.sleep(3)

# 左宙返り
socket.sendto('flip l'.encode('utf-8'),tello_address)
time.sleep(3)

# 右宙返り
socket.sendto('flip r'.encode('utf-8'),tello_address)
time.sleep(3)
socket.sendto('flip f'.encode('utf-8'),tello_address)
time.sleep(3)
socket.sendto('flip b'.encode('utf-8'),tello_address)
time.sleep(3)

socket.sendto('land'.encode('utf-8'),tello_address)
print ('land')