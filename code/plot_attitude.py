#!/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import math
data = np.genfromtxt('EulDataOut.txt', delimiter=' ', skip_header=1,
	skip_footer=1, names=['time', 'roll', 'roll_onb', 'pitch', 'pitch_onb', 'yaw', 'yaw_onb', 'empty1', 'empty2'])

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Attitude estimate")    
ax1.set_xlabel('time (s)')
ax1.set_ylabel('angle (degrees)')

data['roll'] = np.multiply(data['roll'], 180 / math.pi)
data['pitch'] = np.multiply(data['pitch'], 180 / math.pi)
data['yaw'] = np.multiply(data['yaw'], 180 / math.pi)

data['roll_onb'] = np.multiply(data['roll_onb'], 180 / math.pi)
data['pitch_onb'] = np.multiply(data['pitch_onb'], 180 / math.pi)
data['yaw_onb'] = np.multiply(data['yaw_onb'], 180 / math.pi)

ax1.plot(data['time'], data['roll'], color='r', label='roll')
ax1.plot(data['time'], data['pitch'], color='g', label='pitch')
ax1.plot(data['time'], data['yaw'], color='b', label='yaw')

# ax1.plot(data['time'], data['roll_onb'], color='m', label='roll onboard')
# ax1.plot(data['time'], data['pitch_onb'], color='c', label='pitch onboard')
# ax1.plot(data['time'], data['yaw_onb'], color='k', label='yaw onboard')

leg = ax1.legend()

plt.show()