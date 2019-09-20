import numpy as np
import matplotlib.pyplot as plt


#np.random.seed(12345)
#number of times each die is rolled
n=100000

#array for each die with random numbers being output between 1 and 6, running
#n times
die_1 = np.array(np.random.randint(1, 7, n))
die_2 = np.array(np.random.randint(1, 7, n))
die_3 = np.array(np.random.randint(1, 7, n))

#I used functions for each of the separate parts for this question (mostly
#because I didnt know how to use them and wanted to learn) but I understand
#that they don't add anything inparticular to the program apart from readability
#because each function is only called on once.
def larger10_func():
    #adding up each roll and creating a new array with the sums
    sum_array = die_1 + die_2 + die_3
    
    #mask array filled with booleans which are determined by if the sum is 
    #greater than 10 or not
    mask_array = sum_array > 10
    
    #using the length of the mask divided by the number of rolls as a way to
    #work out the probability
    prob = (len(sum_array[mask_array])/n)
    return(prob)
   
def samenum_func():
    #making new arrays filled with booleans for if the values are the same
    same1_array = (die_1 == die_2)
    same2_array = (die_2 == die_3)
    
    #to make sure all three die read the same I need to create a 'master' mask
    #to compare same1_array and same2_array, making sure both are True
    mask_array = same1_array & same2_array == True
    
    #probability is the length of the die_1[mask_array] (all the true values)
    #divided by the total number of rolls
    prob = len(die_1[mask_array])/n
    return(prob)

def cascade_func():
    #creating three arrays fulfilling the conditions from the question. My
    #problem here was comparing three things at once. An if statement would
    #probably have made more sense here.
    threebig2_array = (die_3 > die_2)
    twobig1_array = (die_2 > die_1)
    threebig1_array = (die_3 > die_1)

    #need to create two mask arrays, this was my way of getting around comparing
    #three arrays to eachother. Making an array1 which is a combo of 3>2 and 2>1
    #and then checking to make sure 3 is also > 1.
    mask_array1 = (threebig2_array & twobig1_array == True)
    mask_array2 = (mask_array1 & threebig1_array == True)
    
    prob = len(die_1[mask_array2])/n
    
    return(prob)

#printing the output from each function. Here I am calling the functions within
#the print statement and outputing some text to make it easier to read.
print('Probability of sum larger than 10: ', larger10_func())
print('Probability of same number: ', samenum_func())
print('Probability of 1 < 2 < 3: ', cascade_func())

#I was using these when testing, ensuring that the die rolls and manual prob.
#was correct.
#print('D1 = ', die_1)
#print('D2 = ', die_2)
#print('D3 = ', die_3)