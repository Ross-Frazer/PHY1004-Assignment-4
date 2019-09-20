#importing directories with extra python commands
import numpy as np
import matplotlib.pyplot as plt

#function to estimate pi, no value needs passed to this function so () is empty
#this will only run once called upon in the main chunk of code
def pi_est_func():    
    
    #creating two arrays filled with 100*10 [due to while loop later] random 
    #numbers between -1 and 1
    x_array = np.random.uniform(-1, 1, 100)
    y_array = np.random.uniform(-1, 1, 100)
    
    #this section generates a plot using the x_array and y_array data generated
    #above. '.' sets the points as dots and the colour sets the colour.
    plt.plot(x_array, y_array, '.', color = 'darkolivegreen', markersize = 5)
    plt.xlabel('x_array')
    plt.ylabel('y_array')
    
    #if x**2 + y**2 <= 1 then (x,y) lies within circle. This is the formula
    #for the circle, if the x and y points are <= 1 then they lie inside the 
    #circle. Creates a mask with this stipulation
    circle_plot = (x_array**2 + y_array**2) <= 1
    
    #plotting the data from x/y_array which conforms with the boolean values
    #in the mask. All values which are True will be plotted with a hotpink
    #colour and larger marker size.
    plt.plot(x_array[circle_plot], y_array[circle_plot], '.', color='hotpink', markersize = 10)

    #the calculation used to estimate pi. The idea is to use the ratio of 
    #points inside the circle range vs the total points, giving an area
    #in terms of total number of data points. This was multiplied by 4 due 
    #to how the ratio of a square to a circle worked out. This is explained
    #in the report.
    pi_est = 4*(len(x_array[circle_plot])/(len(x_array))) 
    print(len(x_array))
    #returning the value pi_est when called upon
    return(pi_est)

#this is the main body of the code, it will run before the pi_est_function
#setting n to 1 initially so a random number doesnt get selected instead, I know
#that happens in C but unsure in python.    
n=1

#creating an empty list as an array cannot be added to once it is initialised
#but a list can, this means that I can add to it each time my function is 
#called upon by the while loop below
pi_list=[]

#while loop to iterate 10 times, for the 10 values of pi asked for. Increase
#the number of iterations for a more accurate value of pi
while n<=10:
    #random seed which was used initially during testing. The seed sets a 
    #constant value so that we can run the program multiple times and get
    #the same 'random' value. If this is not used then a random number is
    #generated using the system clock as the seed. 
    #the random seed was placed here to fix a problem I was having where
    #every pi estimate when using a random seed was the same. Making it
    #dependent on how many times the while loop had run solved this.
    b=12345+n
    np.random.seed(b)
    #filling the list with the estimated value of pi from the function above
    pi_list.append(pi_est_func())
    #updating counter
    n=n+1
#creating an array from the list so that the numpy mathematical operations
#of standard deviation and mean can be used, these cannot be used for a list
pi_array = np.array(pi_list)
#printing out the 10 estimated values of pi as well as the mean and std dev.
print('10 Values of Pi = ', pi_list)
print('Pi Mean Value = ', np.mean(pi_array))
print('Pi Standard Deviation = ',np.std(pi_array))