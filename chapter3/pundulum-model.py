# a simple program to analyse chaos of pundulum model
# written by whuCanon, last modified on 2016/04/24

import math
import time
import numpy 
from matplotlib import pyplot
from matplotlib.collections import RegularPolyCollection

k = 1.
q = 0.5
Fd = 1.2
Wd = 2/3.
end_t = 4000


class MotionState:

    def __init__(self, _b=0., _w=0., _t=0.):
        self.b  = _b
        self.w = _w
        self.t  = _t


class Pundulum:

    def __init__(self, state=MotionState(), _Fd = Fd, _dt=0.1):
        self.motionState = []
        self.motionState.append(state)
        self.Fd = _Fd
        self.dt = _dt

    def getNextState(self):
        currentState = self.motionState[-1]
        w  = currentState.w - (k*math.sin(currentState.b) + q*currentState.w - self.Fd*math.sin(Wd*currentState.t)) * self.dt
        b = currentState.b + w * self.dt
        if b > math.pi:
            b -= 2 * math.pi
        elif b < -math.pi:
            b += 2 * math.pi
        self.motionState.append(MotionState(b, w, currentState.t + self.dt))


def plot_regular(ax, i):
    ax.set_xlabel(r'$\theta(radians)$', fontsize=14)
    ax.set_ylabel(r'$\omega(radians/s)$', fontsize=14)
    if i == 0:
        ax.text(2, 1.5, r'$\alpha = 0$', color='black', fontsize=20)
        #ax.text(2, 1.5, r'$\alpha = \pi$', color='black', fontsize=20)
    elif i == 1:
        ax.text(2, 1.5, r'$\alpha = \frac{\pi}{4}$', color='black', fontsize=20)
        #ax.text(2, 1.5, r'$\alpha = \frac{5\pi}{4}$', color='black', fontsize=20)
    elif i == 2:
        ax.text(2, 1.5, r'$\alpha = \frac{\pi}{2}$', color='black', fontsize=20)
        #ax.text(2, 1.5, r'$\alpha = \frac{3\pi}{2}$', color='black', fontsize=20)
    elif i == 3:
        ax.text(2, 1.5, r'$\alpha = \frac{3\pi}{4}$', color='black', fontsize=20)
        #ax.text(2, 1.5, r'$\alpha = \frac{7\pi}{4}$', color='black', fontsize=20)


initState = MotionState(0.2, 0.)
pundulum = Pundulum(initState, Fd, 0.04)

tmp_alpha = [0, 1/8., 1/4., 3/8.]
#tmp_alpha = [1/2., 5/8., 3/4., 7/8.]
tmp_beta  = pundulum.dt*Wd/2/math.pi

fig = pyplot.figure(figsize=(19,12))

ax = []
ax.append(fig.add_subplot(221, xlim=(-4,4), ylim=(-2.5,2.5), autoscale_on=False))
ax.append(fig.add_subplot(222, xlim=(-4,4), ylim=(-2.5,2.5), autoscale_on=False))
ax.append(fig.add_subplot(223, xlim=(-4,4), ylim=(-2.5,2.5), autoscale_on=False))
ax.append(fig.add_subplot(224, xlim=(-4,4), ylim=(-2.5,2.5), autoscale_on=False))

offsets = [[], [], [], []]
collection = [[], [], [], []]
for i in range(4):
    collection[i] = RegularPolyCollection(3, offsets=offsets[i], transOffset=ax[i].transData,)
    ax[i].add_collection(collection[i])
    plot_regular(ax[i], i)

def plot_digram(n):
    global pundulum
    #pundulum = Pundulum(initState, Fd, 0.04)
    for i in range(5000):
        state = pundulum.motionState[0]
        tmp = state.t*Wd/2/math.pi - tmp_alpha[n]
        if math.fabs(tmp - int(tmp)) <= tmp_beta:
            offsets[n].append((state.b, state.w))
            collection[n].set_offsets(offsets[n])
        pundulum.getNextState()
        del pundulum.motionState[0]
    fig.canvas.draw()

def startPlot(event):
    if event.key == 'q':
        while True:
            for i in range(len(ax)):
                plot_digram(i)

fig.canvas.mpl_connect('key_press_event', startPlot)
pyplot.show()