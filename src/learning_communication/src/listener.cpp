

#include <ros/ros.h>  
#include "std_msgs/String.h"
#include <sstream>
#include "geometry_msgs/WrenchStamped.h"
#include "sensor_msgs/JointState.h"
#include <cmath>
#include<fstream>
#include<iostream>

float temp[12] = {0.0};
float *p = &temp[0];
class SubscribeAndPublish  
{  
public:  
  SubscribeAndPublish()  
  {  
    pub_ = n_.advertise<geometry_msgs::WrenchStamped>("/force1", 1000);  
    sub_ = n_.subscribe("force0",1, &SubscribeAndPublish::callback1, this);  
    sub2_ = n_.subscribe("joint_states", 1, &SubscribeAndPublish::callback2, this);  
  }  
//由正向运动学得到变换矩阵的最后一行元素，用于计算实际的接触力
float *qianxiang(const sensor_msgs::JointState::ConstPtr& a)
{
  a1 = a->position[0];
  a2 = a->position[1];
  a3 = a->position[2];
  a4 = a->position[3];
  a5 = a->position[4];
  a6 = a->position[5];
  
  b[0] = sin(a2+a3+a4)*sin(a6)*cos(a5)+cos(a2+a3+a4)*sin(a6);
  b[1] = -sin(a2+a3+a4)*cos(a5)*sin(a6)+cos(a2+a3+a4)*cos(a6);
  b[2] = -sin(a2+a3+a4)*sin(a5);
  return b;
}
  void callback1(const geometry_msgs::WrenchStamped::ConstPtr& msg1)  
  {  
    force.wrench.force.x = msg1->wrench.force.x/1000000+g*x*qq[0]+g*y*qq[1]-fx;
    force.wrench.force.y = msg1->wrench.force.y/1000000-g*y*qq[0]+g*x*qq[1]+fy;
    force.wrench.force.z = msg1->wrench.force.z/1000000+g*qq[2]-fz;
    force.wrench.torque.x = msg1->wrench.torque.x/1000000+g*y*pz*qq[0]-g*x*pz*qq[1]+g*py*qq[2]-tx;
    force.wrench.torque.y = msg1->wrench.torque.y/1000000+g*x*pz*qq[0]+g*y*pz*qq[1]-g*px*qq[2]-ty;
    force.wrench.torque.z = msg1->wrench.torque.z/1000000-g*x*py*qq[0]-g*y*py*qq[1]-g*y*px*qq[0]+g*x*px*qq[1]-tz;
    pub_.publish(force);
    ros::Rate loop_rate(10);
    loop_rate.sleep();
  }  
  
  void callback2(const sensor_msgs::JointState::ConstPtr& msg2)
  {
  qq[0] = qianxiang(msg2)[0];
  qq[1] = qianxiang(msg2)[1];
  qq[2] = qianxiang(msg2)[2];
  for(int i=0;i<3;i++)
      ROS_INFO("[%f]", temp[i]);
  }
private: 
  float a1;
  float a2;
  float a3;
  float a4;
  float a5;
  float a6;
  float g = temp[0];
  float fx = temp[1];
  float fy = -temp[2];
  float fz = temp[3];
  float tx = temp[4];
  float ty = temp[5];
  float tz = temp[6];
  float x = temp[7];
  float y = temp[8];
  float px = temp[9];
  float py = temp[10];
  float pz = temp[11];
  float qq[3];
  float b[3];
  ros::NodeHandle n_;   
  ros::Publisher pub_;  
  ros::Subscriber sub_;
  ros::Subscriber sub2_; 
  geometry_msgs::WrenchStamped force;
  sensor_msgs::JointState joint;

};//End of class SubscribeAndPublish  

int main(int argc, char **argv)  
{  
std::ifstream fin("1.txt");
for(int i = 0;i<12;i++) 
{fin>>*p;           
p++;}   
printf("%d",temp[0]);
fin.close();
  //Initiate ROS  
  ros::init(argc, argv, "subscribe_and_publish");  

  //Create an object of class SubscribeAndPublish that will take care of everything  
  SubscribeAndPublish test;  
  //ros::spin();
  ros::MultiThreadedSpinner s(2);  //多线程
  ros::spin(s);  

  return 0;  
}  


