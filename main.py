#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:38:29 2024

@author: michaelcauson
"""

import numpy as np
import matplotlib.pyplot as plt

pitch_length, pitch_width = 105, 69
kick_length_x = pitch_length/15
kick_length_y = pitch_width/15
score_counter = dict({'Bees': 0, 'Wasps': 0})
x_curr, y_curr = pitch_length/2, pitch_width/2
x, y = [x_curr], [y_curr]

while score_counter['Bees'] + score_counter['Wasps'] < 3:
    f = plt.figure(figsize=(7,7))
    
    plt.rcParams['axes.facecolor'] = 'green'
    plt.subplot(2,1,1)
    plt.plot(x,y,color="white",linestyle="--")
    plt.scatter(x_curr,y_curr,s=40,marker="o",color="white")
    plt.xlim([0,pitch_length])
    plt.ylim([0,pitch_width])
    plt.title("Wasps: " + str(score_counter['Wasps']) + " - "
              + str(score_counter['Bees']) + " Bees")
    
    plt.rcParams['axes.facecolor'] = 'none'
    plt.subplot(2,2,3)
    plt.plot(x)
    plt.ylim([0,pitch_length])
    
    plt.subplot(2,2,4)
    plt.plot(y)
    plt.axhline(y=(1/3)*pitch_width,xmin=0,xmax=pitch_length,color="black",linestyle="--")
    plt.axhline(y=(2/3)*pitch_width,xmin=0,xmax=pitch_length,color="black",linestyle="--")
    plt.ylim([0,pitch_width])
    plt.show()
    
    x_curr = np.maximum(np.minimum(x_curr + np.random.normal(0,kick_length_x),pitch_length),0)
    y_curr = np.maximum(np.minimum(y_curr + np.random.normal(0,kick_length_y),pitch_width),0)
    x.append(x_curr)
    y.append(y_curr)
    
    if y_curr > (1/3)*pitch_width and y_curr < (2/3)*pitch_width:
        if x_curr == 0:
            print("Goal Bees!")
            score_counter['Bees'] += 1
            print(score_counter)
            x_curr, y_curr = pitch_length/2, pitch_width/2
            x = [x_curr]
            y = [y_curr]
        if x_curr == pitch_length:
            print("Goal Wasps!")
            score_counter['Wasps'] += 1
            print(score_counter)
            x_curr, y_curr = pitch_length/2, pitch_width/2
            x = [x_curr]
            y = [y_curr]
 
    f.clear()
    plt.close(f)
    
print("Bees win!" if score_counter['Bees'] == 2 else "Wasps win!")
    