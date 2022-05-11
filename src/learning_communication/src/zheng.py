import sys
sys.path.insert(0, "/home/xsm/pykdl_space/src/hrl-kdl/hrl_geom/src")
sys.path.insert(0, "/home/xsm/orocos_kinematics_dynamics-1.3.2/python_orocos_kdl/build")
from kdl_kinematics import KDLKinematics
from kdl_parser import kdl_tree_from_urdf_model
from urdf_parser_py.urdf import URDF
from copy import deepcopy
from numpy import array,mat
    #  return np.mat([[M[0,0], M[0,1], M[0,2], p.x()],
    #                        [M[1,0], M[1,1], M[1,2], p.y()],
    #                        [M[2,0], M[2,1], M[2,2], p.z()],
    #                        [     0,      0,      0,     1]])
def zheng(q):
    n = mat([0]*36,dtype = float).reshape(6,6)
    robot = URDF.from_xml_file("/home/xsm/control/src/learning_communication/src/ur5_robot.urdf")
    tree = kdl_tree_from_urdf_model(robot)
    chain = tree.getChain("base", "tool0")
    kdl_kin = KDLKinematics(robot, "base_link", "ee_link", tree)
    pose = kdl_kin.forward(q) # forward kinematics (returns homogeneous 4x4 numpy.mat)
    posee = deepcopy(pose)
    pose[2,1] = -pose[2,1]
    pose[2,2] = -pose[2,2]
    pose[0,0] = -pose[0,0]
    pose[1,0] = -pose[1,0]
    posee[:,2] = pose[:,0]
    posee[:,1] = pose[:,2]
    posee[:,0] = pose[:,1]
    n[0:3,0] = pose[0:3,1]  
    n[0:3,1] = pose[0:3,2] 
    n[0:3,2] = pose[0:3,0] 
    n[3:6,3] = pose[0:3,1]  
    n[3:6,4] = pose[0:3,2] 
    n[3:6,5] = pose[0:3,0] 
    return array(n)
def ja(q):
    n = mat([0]*36,dtype = float).reshape(6,6)
    robot = URDF.from_xml_file("/home/xsm/control/src/learning_communication/src/ur5_robot.urdf")
    tree = kdl_tree_from_urdf_model(robot)
    chain = tree.getChain("base", "tool0")
    kdl_kin = KDLKinematics(robot, "base_link", "ee_link", tree)
    pose = kdl_kin.jacobian(q) # forward kinematics (returns homogeneous 4x4 numpy.mat)
    return pose

if __name__ == '__main__':
    print(zheng([-1.59,0,1.59,-1,1.59,0]))
