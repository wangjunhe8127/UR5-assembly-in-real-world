#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, sys
import moveit_commander
import numpy
from numpy import *
from geometry_msgs.msg import WrenchStamped 
from copy import deepcopy
from math import sin,cos
class MoveItFkDemo:
    def __init__(self):
        m = 0
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        # 初始化ROS节点
        rospy.init_node('bianshi', anonymous=True)
        rospy.Publisher("canshu", WrenchStamped, queue_size=1)
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander("manipulator")      
        arm.set_max_velocity_scaling_factor(0.08) 
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001)
        rospy.sleep(1)
        with open('q.txt', 'r') as f:
            data = f.readlines()  # 将txt中所有字符串读入data
            for line in data:
                count = len(data)
                n = 20
                if m == 0:
                    force = [0,1,2,3,4,5]
                    force_sum = array([0,1,2,3,4,5]*20,dtype = float).reshape(20,6)
                    Mean = array([0,1,2,3,4,5]*count,dtype = float).reshape(count,6)
                    R3 = array([0,1,2]*count,dtype = float).reshape(count,3)
                    A1 = array([0,1]*count,dtype = float).reshape(count,2)
                    A2 = array([0,1,2,3]*count*2,dtype = float).reshape(count*2,4)
                    A3 = array([0,1,2,3,4,5]*count*3,dtype = float).reshape(count*3,6)
                    B1 = array([1]*count,dtype = float).reshape(count,1)
                    B2 = array([1]*count*2,dtype = float).reshape(count*2,1)
                    B3 = array([1]*count*3,dtype = float).reshape(count*3,1)
                numbers = line.split()        # 将数据分隔
                numbers_float = map(float, numbers) #转化为浮点数
                numbers_float = array(numbers_float)*pi/180.0
                arm.set_joint_value_target(numbers_float)     
                arm.go()
                rospy.sleep(1)
                while(n!=0):                   
                    ff = deepcopy(rospy.wait_for_message("/force0",WrenchStamped, timeout=None))
                    force[0] = ff.wrench.force.x
                    force[1] = ff.wrench.force.y
                    force[2] = ff.wrench.force.z
                    force[3] = ff.wrench.torque.x
                    force[4] = ff.wrench.torque.y
                    force[5] = ff.wrench.torque.z
                    force_sum[20-n,:] = force
                    n = n-1                
                for i in range(6):
                    Mean[m,i] = numpy.mean(force_sum[:,i])/1000000
                R3[m,0] = sin(numbers_float[1]+numbers_float[2]+numbers_float[3])*cos(numbers_float[4])*cos(numbers_float[5])+cos(numbers_float[1]+numbers_float[2]+numbers_float[3])*sin(numbers_float[5])
                R3[m,1] = -sin(numbers_float[1]+numbers_float[2]+numbers_float[3])*cos(numbers_float[4])*sin(numbers_float[5])+cos(numbers_float[1]+numbers_float[2]+numbers_float[3])*cos(numbers_float[5])
                R3[m,2] = -sin(numbers_float[1]+numbers_float[2]+numbers_float[3])*sin(numbers_float[4])
                m = m+1
        
#####################G、fz#######################
        A1[:,0] = -R3[:,2]
        A1[:,1] = array(ones(count),dtype = float)
        B1 = Mean[:,2]
        P1 = dot(dot(linalg.inv(dot(transpose(A1),A1)),transpose(A1)),B1)
        g = P1[0]
        fz = P1[1]
#####################x,y、fx、fy##################
        for i in range(count):
            A2[i*2,:] = [-g*R3[i,0],-g*R3[i,1],1,0]
            A2[i*2+1] = [-g*R3[i,1],g*R3[i,0],0,1]
            B2[i*2] = Mean[i,0]
            B2[i*2+1] = Mean[i,1]
        P2 = dot(dot(linalg.inv(dot(transpose(A2),A2)),transpose(A2)),B2)
        x = P2[0]
        y = P2[1]
        fx = P2[2]
        fy = P2[3]
#####################px、py、pz、tx、ty、tz#######################
        for i in range(count):
            A3[i*3,:] = [0,-g*R3[i,2],-g*y*R3[i,0]+g*x*R3[i,1],1,0,0]
            A3[i*3+1] = [g*R3[i,2],0,-g*x*R3[i,0]-g*y*R3[i,1],0,1,0]
            A3[i*3+2] = [g*y*R3[i,0]-g*x*R3[i,1],g*x*R3[i,0]+g*y*R3[i,1],0,0,0,1]
            B3[i*3] = Mean[i,3]
            B3[i*3+1] = Mean[i,4]
            B3[i*3+2] = Mean[i,5]
        P3 = dot(dot(linalg.inv(dot(transpose(A3),A3)),transpose(A3)),B3)
        px = P3[0]
        py = P3[1]
        pz = P3[2]
        tx = P3[3]
        ty = P3[4]
        tz = P3[5]
        print("辨识完成！")
        canshu = array([g,fx,fy,fz,tx,ty,tz,x,y,px,py,pz]).reshape(1,12)
        numpy.savetxt("1.txt",canshu,fmt='%f',delimiter=' ')

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)            
if __name__ == "__main__":
    try:
        
        MoveItFkDemo()

    except rospy.ROSInterruptException:
        pass
