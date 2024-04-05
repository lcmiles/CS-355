import numpy as np
import matplotlib.pyplot as plt

train_arrival_times = np.arange(6*60, 24*60, 15) #define the arrival times of the metro train

random_arrival_times = np.random.uniform(7*60+10, 7*60+30, 1000) #generate 1000 random arrival times between 7:10 and 7:30 a.m.

#calculate waiting times for each arrival
waiting_times = [] 
for arrival_time in random_arrival_times:
    next_train_arrival = min(train_arrival_times[train_arrival_times > arrival_time]) #find the next train arrival time after the random arrival time
    waiting_time = next_train_arrival - arrival_time #calculate the waiting time until the next train arrives
    waiting_times.append(waiting_time) #add waotomg to the list

#plot histogram of waiting times
plt.hist(waiting_times, bins=range(0, 16, 2), edgecolor='black') #create a histogram with 2 minute bins
plt.title('Histogram of Waiting Times for Metro Train')
plt.xlabel('Waiting Time (minutes)')
plt.ylabel('Frequency')
plt.xticks(range(0, 16, 2)) #set the ticks for the x-axis
plt.grid(True)
plt.show()

#sources: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/