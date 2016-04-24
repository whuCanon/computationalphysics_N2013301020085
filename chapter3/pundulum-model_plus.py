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


initState = MotionState(0.2, 0.)
pundulum = Pundulum(initState, Fd, 0.04)

tmp_alpha = 0.
tmp_beta  = pundulum.dt*Wd/2/math.pi

fig = pyplot.figure(figsize=(19,12))

ax = fig.add_subplot(111, xlim=(-4,4), ylim=(-2.5,2.5), autoscale_on=False)
ax.set_title(r"$\omega-\theta change$ $with$ $phase$")
ax.set_xlabel(r'$\theta(radians)$', fontsize=14)
ax.set_ylabel(r'$\omega(radians/s)$', fontsize=14)

offsets = []
collection = RegularPolyCollection(3, offsets=offsets, transOffset=ax.transData,)
ax.add_collection(collection)

def plot_digram():
    global pundulum, tmp_alpha
    pundulum = Pundulum(initState, Fd, 0.04)
    del offsets[:]
    tmp_alpha += 1/32.
    tmp_alpha %= 1
    for i in range(500000):
        state = pundulum.motionState[0]
        tmp = state.t*Wd/2/math.pi - tmp_alpha
        if math.fabs(tmp - int(tmp)) <= tmp_beta:
            offsets.append((state.b, state.w))
            collection.set_offsets(offsets)
        pundulum.getNextState()
        del pundulum.motionState[0]
    fig.canvas.draw()

def startPlot(event):
    if event.key == 'q':
        while True:
            plot_digram()

fig.canvas.mpl_connect('key_press_event', startPlot)
pyplot.show()