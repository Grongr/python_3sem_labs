import matplotlib.pyplot as plt
import pandas            as pd
import numpy             as np

from sys import platform

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

    frame = []
    for i in range(len(x) - 1):
        plt.axis([0, max(all_data), min(all_data) - abs(min(all_data)/5),
                 max(all_data) + abs(max(all_data)/5)])
        plt.plot(x[i],y[i])
        plt.grid(True)
       
        plt.title(f'Frame: {i + 1}') 
        plt.savefig(f'{i+1}.png')
        frame.append(f'{i+1}.png')
        plt.clf()
        
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in frame:
            image = imageio.imread(filename)
            writer.append_data(image)
        for filename in frame:
            os.remove(filename)

    if platform == 'linux' or platform == 'linux2':
        os.system("xviewer " + r"mygif.gif")
    elif platform == 'win32' or platform == 'win64':
        os.startfile(r'mygif.gif')
    else:
        raise Exception("Undefined platform.")
    time.sleep(2)
    os.remove('mygif.gif')
    
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

    # second_task()

    third_task()
