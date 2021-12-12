import matplotlib.pyplot as plt
import numpy             as np

from matplotlib.animation import FuncAnimation
from PIL                  import Image

def first_task():
    for i in range(1, 4):
        data = np.array(Image.open('pics/lunar0' + str(i) + '_raw.jpg'))
        updated_data = (data - data.min()) * int(255/(data - data.min()).max())
        res_img = Image.fromarray(updated_data)
        res_img.save('pics/result/res_' + str(i) + '.jpg')

def second_task():
    fig, axs = plt.subplots(nrows=3, ncols=2)
    fig.set_figheight(9)
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
    coords = [[0, 0], [1, 0], [2, 0]]

    for num, coord in zip(range(1, 4), coords):
        initial_y = np.loadtxt('signals/signal0' + str(num) + '.dat')
        x = np.arange(len(initial_y))
        upd_y = np.zeros(len(x))
        upd_y[0: 10] = np.cumsum(initial_y[0:10]) / np.arange(1, 11)
        upd_y[10:] = np.convolve(initial_y, np.ones(11) / 10, mode='valid')
        left = axs[coord[0]][coord[1]]
        left.plot(x, initial_y)
        left.set_xlim([x.min(), x.max()])
        left.set_ylim([1.1 * initial_y.min(), 1.1 * initial_y.max()])
        left.grid()
        left.set_title('Сырой сигнал ' + str(num))
        right = axs[coord[0]][coord[1] + 1]
        right.plot(x, upd_y)
        right.set_xlim([x.min(), x.max()])
        right.set_ylim([1.1 * initial_y.min(), 1.1 * initial_y.max()])
        right.grid()
        right.set_title('После фильтра ' + str(num))

    plt.savefig('./signals/result/signal.png')
    
vector_u = np.loadtxt('func/func.dat')
x = np.arange(len(vector_u))
def third_task():
    plt.style.use('seaborn-pastel')

    N = 255
    matrix_A = np.eye(len(vector_u)) - np.eye(len(vector_u), k=-1)
    matrix_A[0][-1] = -1

    fig = plt.figure()
    ax = plt.axes(xlim=(0, len(x)), ylim=(0, 1.1 * max(vector_u)))
    line, = ax.plot([], [])


    def animate(i):
        global x, vector_u
        vector_u = vector_u - 0.5 * matrix_A @ vector_u
        line.set_data(x, vector_u)
        return line,


    anim = FuncAnimation(fig, animate, frames=N, interval=10, blit=True)
    anim.save('func/result/gif.gif', writer='pillow')

if __name__ == "__main__":

    print("##################################################")
    print("------------------------Firts---------------------")
    first_task()

    print("##################################################")
    print("----------------------Second----------------------")
    second_task()

    print("##################################################")
    print("-----------------------Third----------------------")
    third_task()
