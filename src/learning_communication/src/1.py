#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import time 
# import urx
# import logging


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     rob = urx.Robot("192.168.1.12")
#     try:
#         rob.speedj([0.2,0.507286033,0.115075356,0.0512183314,0.000526721089,0.124454971],1,min_time = 0.008)
#     finally:
#         rob.close()
import numpy as np
import socket
import time
import struct
import util
import rtde
HOST ='192.168.1.12'   
PORT = 30003		
ADDR = (HOST,PORT)
robot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
robot.connect(ADDR)

str_command = "speedj([0,0.1,0,0,0,0],0.1,1)" 
robot.send(str_command + "\n")
robot.close()
while(1):
    HOST ='192.168.1.12'   
    PORT = 30003		
    ADDR = (HOST,PORT)
    robot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    robot.connect(ADDR)
    str_command = "speedj([0.1,0,0,0,0,0],0.1,1)" 
    robot.send(str_command + "\n")
    robot.close()
