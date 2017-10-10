#!/usr/bin/env python
# -------------------------------
# DQN for NAO and skin
# Author: Tianming Qiu
# Date: 2017.Sep.29
# All rights reserved
# -------------------------------

import rospy
import sys
from naoqi import ALProxy
import time
import tensorflow as tf 
import numpy as np 
import random
from collections import deque
import roslib; roslib.load_manifest('numpy_tutorial')
from std_msgs.msg import Float32MultiArray
from rospy_tutorials.msg import Floats
import math


class ENV():
    def __init__(self):
        self.reward = 0
        self.state = 1
        self.guide = 0
        self.joint = (0,0)
        self.state_dim = 2
        self.action_dim = 4
        self.dev = 0
        self.in_out = (0,0)


        #self.data = [0.0234375, 0.0263671875, 0.021484375, 0.012044270522892475, 0.0074869790114462376, 0.01725260354578495, 0.01790364645421505, 0.01692708395421505, 0.015625, 0.014973958022892475, 0.0146484375, 0.013671875, 0.009114583022892475, 0.013346354477107525]


    def calReward(self):
        rospy.Subscriber("force_hand", Float32MultiArray, self.reward_CB)
        return self.reward, self.guide,self.dev,self.in_out
    def reward_CB(self, data):
        cell_sum = 0
        # calculate reward according to skin cell with different weightings
        for i in range(14):
            cell_sum = cell_sum + data.data[i]
        #self.reward = - (self.reward + 5 * (data.data[0] + data.data[1] + data.data[9] + data.data[11]))
        
        # below need to be tested:
        
        part_out = 3 * data.data[0] + data.data[1] + data.data[9] + 5 * data.data[11]
        part_in = cell_sum - part_out + 5 * data.data[3] + 5 * data.data[8]
        part_in = part_in / 20
        part_out = part_out / 10
        deviation = part_out - 2 * part_in
        #print deviation
        if deviation <= -0.01:
            self.guide = -1
        elif deviation >= 0.015:
            self.guide = 1
        else: 
             self.guide = 0

        self.reward = - (part_out + part_in)
        self.dev = deviation
        self.in_out = (part_in,part_out)



if __name__ == '__main__':
    rospy.init_node('guide_reward_test_node', anonymous = False)
    env = ENV()
    while not rospy.is_shutdown():
        reward,guide,deviation,in_out = env.calReward()
        time.sleep(0.2)
        reward,guide,deviation,in_out = env.calReward()
        #print cell_data
        reward = round(reward, 4)
        deviation = round(deviation, 4)
        a = [0,0]
        a[0] = round(in_out[0],5)
        a[1] = round(in_out[1],5)

        #for i in range(14):
            #print "Cell_%s: %s" %(i, cell_data[i])
        print "==================================================================="
        
        #part_in = (cell_data[2]+cell_data[3]+cell_data[4]+cell_data[5]+cell_data[6]+cell_data[7]+cell_data[8]+cell_data[10]+cell_data[12]+cell_data[13]) / 10
        #part_out = (cell_data[0] + cell_data[1] + cell_data[9] + cell_data[11]) / 4
        #deviation =part_out - part_in
        #print "out(+)/in(-): %s" %(part_out - part_in)


        print "Reward: %s, Guide: %s, Deviation: %s, In & Out: %s" %(reward,guide,deviation,a)
        

        time.sleep(3)