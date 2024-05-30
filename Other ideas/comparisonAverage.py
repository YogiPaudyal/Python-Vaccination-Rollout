# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:42:31 2021

@author: Allan
"""

numbers = [12,47,50, 300, 27, 90, 3, 200]
names = ["james","john","jeremy","jude","philip","terry","claire","ian"]

# function to combine the two lists

def combiner(names,numbers): 
    global z
    z = dict(zip(names,numbers))
    return z
combiner(names,numbers)
# this ensures the two lists are sorted from the lowest to highest based
# on the values

b = sorted(z.items(),key=lambda x: x[1])

# assigning the lowest and highest values variables
highest_value = b[0]
lowest_value = b[-1]

print("The highest value pair is : ", highest_value,"\nthe lowest value pair is: ",lowest_value)
       
# function to calculate the mean 
def average(x):
    total = 0
    for digit in x:
        total += digit
    
    average = total/len(x)
    
    print("\n the average value is :", average)

average(numbers)
