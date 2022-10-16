#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    New_N=round(N)
    
if N > 20: 
    if New_N%2 == 0:
        print("Not Weird")
    else: 
        print("Weird")
elif New_N <=20 and New_N >= 6:
    if New_N%2==0:
        print("Weird")
    else:
        print("Weird")
elif New_N>=2 and New_N<=5:
    if New_N%2==0:
        print("Not Weird")
    else:
        print("Weird")



# Objective:
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

# Task:
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not is weird.