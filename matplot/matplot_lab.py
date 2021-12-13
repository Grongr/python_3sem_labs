import matplotlib.pyplot as plt
import pandas            as pd
import numpy             as np

from matplotlib.animation import FuncAnimation
from sys                  import platform

import imageio
import time
import math
import sys
import os

def first_task(calculate_size=False):

    names = ['001.dat', '002.dat',
             '003.dat', '004.dat',
             '005.dat']

    for i in names:
        plot_one_in_first(i, calculate_size=calculate_size)

def plot_one_in_first(filename, calculate_size=False):
    with open(filename, 'r') as f:
        data = f.readlines()

    x = []
    y = []
    for i in range(1, int(data[0]) + 1):
        x.append(float(data[i].split()[0]))
        y.append(float(data[i].split()[1]))
        
    if calculate_size:
        if math.sqrt(x[0] ** 2 + y[0] ** 2) != 0:
            points_size = math.sqrt(x[0] ** 2 + y[0] ** 2)
        else:
            points_size = 10000000
            
        for a, b in zip(x, y):
            for c, d in zip(x, y):
                current_size = math.sqrt((a - c) ** 2 + (b - d) ** 2)
                if points_size > current_size > 0:
                    points_size = current_size

        points_size *= 0.5
    else:
        points_size = 10
        
    plt.plot(x, y, '.', markersize=points_size)
    plt.axis('scaled')
    plt.title(f'Number of points: {data[0]}')
    plt.show()

def second_task():
    """ Solves second task in matplotlib lab. """

    filename = 'data.dat'

    with open(filename, 'r') as f:   
        data = (f.read().split('\n'))

    for i in range(len(data)):
        data[i] = list(map(float, data[i].split()))

    x = []
    y = []
    for i in range(len(data)):
        if i % 2 != 0:
            y.append(data[i])
        else: 
            x.append(data[i])

    all_data = []
    for i in data:
        all_data += i

    fig, ax = plt.subplots()
    line, = ax.plot(x[5], y[5])

    def anim(i, line, x, y, ax):
        line.set_data(x[i], y[i])
        plt.title(f"Frame: {i + 1}")
        plt.grid(True)
        return [line]

    animation = FuncAnimation(
            fig,
            func=anim,
            frames=np.arange(0, len(y)),
            fargs=(line, x, y, ax),
            blit=True,
            repeat=True
            )

    animation.save("mygif.gif", writer='imagemagick')
    plt.show()
    
def third_task():
    dk = pd.read_csv('students.csv', sep=";", header=None)
    dk.columns = ['prep','group', 'marks']
    test5 = dk.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
    test6 = dk.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
    test5.plot(kind='bar', stacked=True, rot= 0)
    test6.plot(kind='bar', stacked=True, rot= 0)
    plt.show()

if __name__ == "__main__":

    # first_task()

    second_task()

    # third_task()
