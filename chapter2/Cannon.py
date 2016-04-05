# a simple program to analyse cannon shell's trail
# written by whuCanon, last modified on 2016/04/04

from pylab import *
import thread
import math

# some arguments
g = 9.8
B2m = 4e-5
initSpeed = 1000.
hit_area = 10.
sita = math.pi / 2


class FlightState:

    def __init__(self, _x=0, _y=0, _v_x=0, _v_y=0, _t=0):
        self.x  = _x
        self.y  = _y
        self.v_x = _v_x
        self.v_y = _v_y
        self.t  = _t


class CannonShell:

    def __init__(self, _fs=FlightState(), _dt=0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt

    def getNextState(self):
        currentState = self.flightState[-1]
        x  = currentState.x + currentState.v_x * self.dt
        y  = currentState.y + currentState.v_y * self.dt
        v_x = currentState.v_x + self.getCurrentAcc(currentState)[0] * self.dt
        v_y = currentState.v_y + self.getCurrentAcc(currentState)[1] * self.dt
        self.flightState.append(FlightState(x, y, v_x, v_y, currentState.t + self.dt))

    def getCurrentAcc(self, currentState):
        factor = self.getFactor(currentState)
        a_x = factor * (-B2m * currentState.v_x**2)
        a_y = factor * (-B2m * currentState.v_y**2) - g
        currentAcc = [a_x, a_y]
        return currentAcc

    def getFactor(self, currentState):
        alpha = 2.5
        a = 6.5e-3
        factor = 0
        try:
            factor = (1 - a * currentState.y / 288.15)**alpha
        except ValueError, e:
            print e
        return factor


def display(cannonShell):
    # get the minimal and maximal value
    x, y = [], []
    for flightState in cannonShell.flightState:
        x.append(flightState.x)
        y.append(flightState.y)
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    # adjust the diagram
    dy = (ymax - ymin) * 0.1
    ylim(ymin, ymax + dy)
    # add label
    xticks([target[0]])
    yticks([target[1]])
    # add auxiliary line
    plot([0,xmax],[target[1],target[1]], color='red', linewidth=2.5, linestyle="--")
    # name the axis
    xlabel(r'$x(m)$', fontsize=16)
    ylabel(r'$y(m)$', fontsize=16)
    # plot
    plot(x, y, "blue", label="shootingTrail")
    legend(loc='upper center')


def calculate(target):
    initState = FlightState(0., 0., initSpeed * math.cos(sita), initSpeed * math.sin(sita))
    cannonShell = CannonShell(initState, 1)
    while True:
        if cannonShell.flightState[-1].y < target[1] and cannonShell.flightState[-1].v_y < 0:
            break
        cannonShell.getNextState()
    return cannonShell


def storeData(target, accuracy):
    #savefig("shootingTrail.png",dpi=256)
    f = open("shootParadise.txt", "w")
    print >> f, "Target position:\n\tX: %f \n\tY: %f \n" % (target[0], target[1])
    print >> f, "Shooting angle: %f \nShooting Speed: %f\n" % (sita, initSpeed)
    print >> f, "Attacking accuracy: %f " % (accuracy)
    f.close()


def shoot():
    print "sita: ", sita
    print "initSpeed: ", initSpeed


farthest_x = 0
target = [20000, 2000]
#target.append(float(raw_input("Please input the target's X_position: ")))
#target.append(float(raw_input("Please input the target's Y_position: ")))

for i in range(100):
    sita -= math.pi / (2 * 100)
    cannonShell = calculate(target)
    #display(cannonShell)
    if farthest_x < cannonShell.flightState[-1].x:
        farthest_x = cannonShell.flightState[-1].x
    else:
        break

for i in range(1000):
    initSpeed -= 1
    cannonShell = calculate(target)
    #display(cannonShell)
    accuracy = math.fabs(cannonShell.flightState[-1].x - target[0])
    if accuracy < hit_area:
        shoot()
        storeData(target, accuracy)
        break
