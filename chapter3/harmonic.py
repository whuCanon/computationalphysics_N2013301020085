# a simple program to analyse hamonic and anhamonic oscillator
# written by whuCanon, last modified on 2016/04/18

import math
import numpy 
from matplotlib import pyplot

k = 1
end_t = 40
amplitude = [1, 0.5, 0.2]
alpha = [1, 3]


class MotionState:

    def __init__(self, _b=0., _w=0., _t=0.):
        self.b  = _b
        self.w = _w
        self.t  = _t


class Oscillator:

    def __init__(self, state=MotionState(), _alpha = alpha[0], _dt=0.1):
        self.motionState = []
        self.motionState.append(state)
        self.alpha = _alpha
        self.dt = _dt

    def getNextState(self):
        currentState = self.motionState[-1]
        w  = currentState.w - k * currentState.b**self.alpha * self.dt
        b = currentState.b + w * self.dt
        self.motionState.append(MotionState(b, w, currentState.t + self.dt))


def calculate(amplitude, alpha):
    initState = MotionState(amplitude, 0.)
    oscillator = Oscillator(initState, alpha, 0.01)
    while True:
        if oscillator.motionState[-1].t >= end_t:
            break
        oscillator.getNextState()
    return oscillator


def plot_regular(i):
    xmin, xmax = 0 , end_t
    ymin, ymax = -1, 1
    dy = (ymax - ymin) * 0.2
    ax = pyplot.axes(xlim=(xmin, xmax), ylim=(ymin - dy, ymax + dy))
    # add describe text
    if i == 0:
        pyplot.title("hamonic oscillator")
        pyplot.text(35, 1.1, r'$\alpha = 1$' + '\n' + r'$k = 1$', color='black', fontsize=20)
    elif i == 1:
        pyplot.title("anhamonic oscillator")
        pyplot.text(35, 1.1, r'$\alpha = 3$' + '\n' + r'$k = 1$', color='black', fontsize=20)
    # name the axis
    pyplot.xlabel(r'$time(s)$', fontsize=20)
    pyplot.ylabel(r'$\theta(radians)$', fontsize=20)


for i in range(len(alpha)):
    fig = pyplot.figure(figsize=(19,12))
    plot_regular(i)
    for j in range(len(amplitude)):
        x = []
        y = []
        oscillator = calculate(amplitude[j], alpha[i])
        for state in oscillator.motionState:
            x.append(state.t)
            y.append(state.b)
        pyplot.plot(x, y, label="amplitude="+str(amplitude[j]))
    pyplot.legend(loc='lower right')
    pyplot.savefig("oscillator_"+str(i)+".png",dpi=72)

pyplot.show()