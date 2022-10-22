#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    totalNumberofswaps = 0
    for i in range(0,n):
        numberOfSwaps = 0;
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                tmp =a[j]
                a[j]=a[j+1]
                a[j+1] = tmp
                numberOfSwaps +=1
        totalNumberofswaps += numberOfSwaps
        
        if (numberOfSwaps == 0):
            break;

    # Write your code here
    
    print('Array is sorted in '+str(totalNumberofswaps)+' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[n-1]))
    
    

# Task: 
# Given an array, , of size  distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:
# Array is sorted in numSwaps swaps. 
# where  is the number of swaps that took place.
# First Element: firstElement 
# where  is the first element in the sorted array.
# Last Element: lastElement 
# where  is the last element in the sorted array.
# Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.