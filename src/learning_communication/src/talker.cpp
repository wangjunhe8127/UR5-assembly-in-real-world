/**
 * 该例程将发布chatter话题，消息类型String
 */
 
#include <sstream>
#include "ros/ros.h"
#include "geometry_msgs/WrenchStamped.h"
#include <stdio.h>

#ifdef __cplusplus
extern "C"
{
#endif
#include "netft.h"
#ifdef __cplusplus
}
#endif
int main(int argc, char **argv)
{
    // ROS节点初始化
    ros::init(argc, argv, "talker");

    // 创建节点句柄
    ros::NodeHandle n;

    // 创建一个Publisher，发布名为chatter的topic，消息类型为std_msgs::String
    ros::Publisher chatter_pub = n.advertise<geometry_msgs::WrenchStamped>("force0", 1000);

    // 设置循环的频率
    ros::Rate loop_rate(100);

    int nn = 0;

    int count = 0;

    while (ros::ok())
    {
        // 初始化std_msgs::String类型的消息
        geometry_msgs::WrenchStamped msg;
        msg.wrench.force.x = a(argc,argv)[0];
        msg.wrench.force.y = a(argc,argv)[1];
        msg.wrench.force.z = a(argc,argv)[2];
        msg.wrench.torque.x = a(argc,argv)[3];
        msg.wrench.torque.y = a(argc,argv)[4];
        msg.wrench.torque.z = a(argc,argv)[5];
        // 发布消息
ROS_INFO("[%f]", msg.wrench.force.x);
        chatter_pub.publish(msg);

        // 循环等待回调函数
        ros::spinOnce();

        // 按照循环频率延时
        loop_rate.sleep();
        ++count;
    }

    return 0;
}
