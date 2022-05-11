#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, sys
import moveit_commander
from numpy import linalg,array,reshape,dot,transpose,any,matlib
from geometry_msgs.msg import WrenchStamped 
from copy import deepcopy
import numpy as np
import socket
import time
import struct
import util
import rtde
from zheng import zheng
from nizhuan import nizhuan,ja
from R2oula import rotationMatrixToEulerAngles
import termios, sys, os
TERMIOS = termios
zhuan = array([0,0,0,0,0,0]*6,dtype = float).reshape(6,6)
a = 0.5
t = 0.08
HOST ='192.168.1.12'   
PORT = 30003		
ADDR = (HOST,PORT)
global fanhui,ffx,ffy,ffz,ttx,tty,ttz,biaozhi,lujing,key,number,oula,x,y,z,zhi
key = 'o'
fanhui = 0
biaozhi = 0
lujing = []
ffx = 0
ffy = 0
ffz = 0
ttx = 0
tty = 0
ttz = 0
number = 0
oula = 0
x = 0
y = 0
z = 0
zhi = 0
def getkey():
	fd = sys.stdin.fileno()
	old = termios.tcgetattr(fd)
	new = termios.tcgetattr(fd)
	new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
	new[6][TERMIOS.VMIN] = 1
	new[6][TERMIOS.VTIME] = 0
	termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
	c = None
	try:
	    c = os.read(fd, 1)
	finally:
	    termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
	return c
def chongxian():
    while(1):
        if globals()['fanhui'] == 1:
            for i in range(len(globals()['lujing'])):
                arm.set_joint_value_target(globals()['lujing'][len(globals()['lujing'])-i-1])     
                arm.go()
                rospy.sleep(0.1)
            globals()['fanhui'] = 0
            globals()['lujing'] = []
            globals()['key'] = 'o'
            print("已回到初始点，开始参数重新调整")
        else:
            if globals()['biaozhi']  == 1:
                globals()['key'] = 'g'
            if getkey().decode() == 'f':
                globals()['key'] = 'f'
                globals()['fanhui'] = 1
                globals()['biaozhi'] = 0
                print("原路返回")
            elif getkey().decode() == 'g':
                globals()['key'] = 'g'
                print("开始实验")
            #这一句显然不会运行
            else:
                globals()['key'] = 'o'
def callback(data):  
    if  globals()['fanhui'] == 0:
        globals()['number'] =globals()['number']+1
        dikaer = [[1.0],[2.0],[3.0],[4.0],[5.0],[6.0]]
        dikaer[0] = data.wrench.force.x+globals()['ffx'] if abs(data.wrench.force.x+globals()['ffx'])>1 else 0
        dikaer[1] = data.wrench.force.y+globals()['ffy'] if abs(data.wrench.force.y+globals()['ffy'])>1 else 0
        dikaer[2] = data.wrench.force.z+globals()['ffz'] if abs(data.wrench.force.z+globals()['ffz'])>1.5 else 0
        dikaer[3] = data.wrench.torque.x+globals()['ttx'] if abs(data.wrench.torque.x+globals()['ttx'])>1 else 0
        dikaer[4] = data.wrench.torque.y+globals()['tty'] if abs(data.wrench.torque.y+globals()['tty'])>1 else 0
        dikaer[5] = data.wrench.torque.z+globals()['ttz'] if abs(data.wrench.torque.z+globals()['ttz'])>1 else 0
        
        if (globals()['biaozhi'] == 0):
            globals()['ffx'] = -data.wrench.force.x
            globals()['ffy'] = -data.wrench.force.y
            globals()['ffz'] = -data.wrench.force.z
            globals()['ttx'] = -data.wrench.torque.x
            globals()['tty'] = -data.wrench.torque.y
            globals()['ttz'] = -data.wrench.torque.z
        # print(globals()['key'],globals()['biaozhi'],globals()['fanhui'])
        if (globals()['key'] == 'g') or (globals()['biaozhi']  == 1): 
            globals()['biaozhi']  = 1
            current_joint_values=arm.get_current_joint_values()
            globals()['lujing'].append(current_joint_values)
        #首先没有系数
        #######################3
            # dikaer = dikaer*0.01
            dikaer = dot(zhuan,dikaer)
######判断角度######
            z=1

            if (abs(nizhuan(current_joint_values)[2,2])>0.996):
                globals()['zhi'] = 1
            if (abs(nizhuan(current_joint_values)[2,2])<0.996) and (globals()['oula']==0) and globals()['zhi'] == 0:
                globals()['w'] = rotationMatrixToEulerAngles(nizhuan(current_joint_values))[2]*10
                globals()['y'] = rotationMatrixToEulerAngles(nizhuan(current_joint_values))[1]*10
                globals()['x'] = rotationMatrixToEulerAngles(nizhuan(current_joint_values))[0]*10
                z = 0 
                globals()['oula']=1
            if globals()['oula']==3:
                z = 0 
                dikaer[0] = 0.0
                dikaer[1] = 0.0
                dikaer[2] = 0.0
                dikaer[3] = 0.0
                dikaer[4] = 0.0
                dikaer[5] = globals()['w']
                globals()['oula']=0
            if globals()['oula']==2:
                z = 0 
                dikaer[0] = 0.0
                dikaer[1] = 0.0
                dikaer[2] = 0.0
                dikaer[3] = 0.0
                dikaer[4] = globals()['y']
                dikaer[5] = 0.0
                globals()['oula']=3
            if globals()['oula']==1:
                z = 0 
                dikaer[0] = 0.0
                dikaer[1] = 0.0
                dikaer[2] = 0.0
                dikaer[3] = globals()['x']
                dikaer[4] = 0.0
                dikaer[5] = 0.0
                globals()['oula']=2
            # start_pose = arm.get_current_pose(eef_link).pose
            # rospy.INFO(start_pose)
            # print (nizhuan(current_joint_values))
            # wpose = deepcopy(start_pose)
            current_jacobian_matrix=matlib.zeros((6,6))	
            current_jacobian_matrix=ja(current_joint_values)

            current_jacobian_matrix[0,:] = -current_jacobian_matrix[0,:]
            current_jacobian_matrix[1,:] = -current_jacobian_matrix[1,:]	
            current_jacobian_matrix[3,:] = -current_jacobian_matrix[3,:]
            current_jacobian_matrix[4,:] = -current_jacobian_matrix[4,:]
            # print(current_jacobian_matrix.dtype)
            # print(current_jacobian_matrix)
            # print("lallallala")
            print(nizhuan(current_joint_values))
            # print(arm.get_jacobian_matrix(current_joint_values)	)
            print("ddddddd")
   
        #######################1
            #joint = transpose(dot(dot(linalg.pinv(current_jacobian_matrix),zheng(current_joint_values)),dikaer*0.01))
        #######################2
            
            joint1 = dot(zheng(current_joint_values),dikaer)
            
        #######################fz取值 固定

        #######################fz取值 卡尔曼滤波
            if z == 1:
                joint1[2] = -0.2
            joint = transpose(dot(linalg.pinv(current_jacobian_matrix),joint1))

            jointt= joint*0.03
            # print(jointt)
            joint = array([0.0,0.0,0.0,0.0,0.0,0.0])
            # joint = sum(joint,[])
            # print(jointt)
      
            for i in range(6):
                joint[i] = float(jointt[i,0])
            print("jjj")
            # print(joint[0])
        #######################
            # joint = transpose(dot(dot(linalg.pinv(current_jacobian_matrix),zheng(current_joint_values)),dikaer))
            if (z == 1) and (globals()['number'] > 5):
                robot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
                robot.connect(ADDR)
                str_command = "speedj([%(q1)s,%(q2)s,%(q3)s,%(q4)s,%(q5)s,%(q6)s],a=%(a)s,t=%(t)s)" %{'q1':joint[0],'q2':joint[1],'q3':joint[2],'q4':joint[3],'q5':joint[4],'q6':joint[5],'a':a,'t':t}
                robot.send(str_command + "\n")
                robot.close()
            if (z == 0):
                robot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
                robot.connect(ADDR)
                # print(joint)
                str_command = "speedj([%(q1)s,%(q2)s,%(q3)s,%(q4)s,%(q5)s,%(q6)s],a=%(a)s,t=%(t)s)" %{'q1':joint[0],'q2':joint[1],'q3':joint[2],'q4':joint[3],'q5':joint[4],'q6':joint[5],'a':a,'t':t}
                robot.send(str_command + "\n")
                robot.close()
            if(globals()['number'] > 5):
                globals()['number'] = 0
if __name__ == "__main__":
    try: 
        print(globals())
                # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        # 初始化ROS节点
        rospy.init_node('kongzhi', anonymous=True)
        rospy.Subscriber("/force1_throttle", WrenchStamped, callback)
        # 初始化需要使用move group控制的机械臂中的arm .group
        arm = moveit_commander.MoveGroupCommander("manipulator") 
        arm.set_planner_id('RRTConnectkConfigDefault')
        arm.set_planning_time(5)
        arm.set_max_velocity_scaling_factor(0.06) 
        arm.set_end_effector_link('tool0')
        arm.set_pose_reference_frame('base_link')
        arm.allow_replanning(True)
        eef_link = arm.get_end_effector_link()     
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001) 
        with open('1.txt', 'r') as f:
            data = f.readlines()  # 将txt中所有字符串读入data
            for line in data:
                numbers = line.split()        # 将数据分隔
                numbers_float = map(float, numbers) #转化为浮点数
                x = array(numbers_float)[7]
                y = array(numbers_float)[8]
                px = array(numbers_float)[9]
                py = array(numbers_float)[10]
                pz = array(numbers_float)[11]
        zhuan[0,0] = x
        zhuan[0,1] = -y
        zhuan[1,0] = y
        zhuan[1,1] = x
        zhuan[2,2] = 1
        zhuan[3,3] = x
        zhuan[3,4] = -y
        zhuan[3,5] = 1
        zhuan[3,0] = 2*x*y*pz
        zhuan[3,1] = -y*y*pz+x*x*pz
        zhuan[3,2] = -x*py-y*px
        zhuan[4,0] = -x*x*pz+y*y*pz
        zhuan[4,1] = 2*x*y*pz
        zhuan[4,2] = -y*px+x*py
        zhuan[5,0] = x*py-y*px
        zhuan[5,1] = -y*py-x*px
        zhuan[4,3] = y
        zhuan[4,4] = x
        chongxian()
    except rospy.ROSInterruptException:
        pass

