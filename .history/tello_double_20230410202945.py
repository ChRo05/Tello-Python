# 実際のプログラム

import socket
import time

drone1 = '192.168.137.125'
drone2 = '192.168.137.17'

tello_port = 8889

#udpソケット
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone1_address = (drone1 , tello_port)
drone2_address = (drone2 , tello_port)

#コマンドモードに入る
socket.sendto('command'.encode('utf-8'),drone1_address)
socket.sendto('command'.encode('utf-8'),drone2_address)

#離陸
socket.sendto('takeoff'.encode('utf-8'),drone1_address)
socket.sendto('takeoff'.encode('utf-8'),drone2_address)

time.sleep(3)

# 左へ回転
socket.sendto('left 50'.encode('utf-8'),drone1_address)
# 右へ回転
socket.sendto('right 50'.encode('utf-8'),drone2_address)

time.sleep(3)

# 前進
socket.sendto('forward 50'.encode('utf-8'),drone1_address)
socket.sendto('forward 50'.encode('utf-8'),drone1_address)

time.sleep(3)

# 左へ宙返り
socket.sendto('flip l'.encode('utf-8'),drone1_address)
socket.sendto('flip l'.encode('utf-8'),drone2_address)

# 右へ宙返り
socket.sendto('flip r'.encode('utf-8'),drone1_address)
socket.sendto('flip r'.encode('utf-8'),drone2_address)

# 前方へ宙返り
socket.sendto('flip f'.encode('utf-8'),drone1_address)
socket.sendto('flip f'.encode('utf-8'),drone2_address)

# 後方へ宙返り
socket.sendto('flip b'.encode('utf-8'),drone1_address)
socket.sendto('flip b'.encode('utf-8'),drone2_address)

time.sleep(3)

#着陸
socket.sendto('land'.encode('utf-8'),drone1_address)
socket.sendto('land'.encode('utf-8'),drone2_address)

