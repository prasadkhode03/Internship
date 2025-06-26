'''15.	Moving Averages:
o	Given an array of daily temperatures, write a NumPy script to compute a 3 day moving average.'''
import numpy as np
temperatures = np.array([25, 27, 23, 24, 26, 28, 29, 27, 25, 24])
moving_avg = np.convolve(temperatures, np.ones(3)/3, mode='valid')
print("3-Day Moving Average:", moving_avg)