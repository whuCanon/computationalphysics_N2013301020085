# a simple program to analyse cannon shell's trail
# written by whuCanon, last modified on 2016/04/04

import sys
import math
import time
from visual import *

# some arguments
g = vector(0, -9.8, 0)
B2m = 4e-5
initSpeed = 1000.
hit_area = 10.
sign = 1
latitude = 30 * math.pi / 180
selfRotation = vector(0, 7.292e-5*math.sin(latitude), -7.292e-5*math.cos(latitude))

# some global variate
farthest_d = 0
target = [20000., 2000., 20000.]
# target.append(float(raw_input("Please input the target's X_position: ")))
# target.append(float(raw_input("Please input the target's Y_position: ")))
# time.sleep(10)
theta = 0.5
cosf = target[0] / math.sqrt(target[0]**2 + target[2]**2)
sinf = target[2] / math.sqrt(target[0]**2 + target[2]**2)


class FlightState:

    def __init__(self, _x=0., _y=0., _z=0., _v_x=0., _v_y=0., _v_z=0., _t=0.):
        self.x  = _x
        self.y  = _y
        self.z = _z
        self.v_x = _v_x
        self.v_y = _v_y
        self.v_z = _v_z
        self.t  = _t


class CannonShell:

    def __init__(self, _fs=FlightState(), _dt=0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt

    def getNextState(self):
        currentState = self.flightState[-1]
        x   = currentState.x + currentState.v_x * self.dt
        y   = currentState.y + currentState.v_y * self.dt
        z   = currentState.z + currentState.v_z * self.dt
        v_x = currentState.v_x + self.getCurrentAcc(currentState)[0] * self.dt
        v_y = currentState.v_y + self.getCurrentAcc(currentState)[1] * self.dt
        v_z = currentState.v_z + self.getCurrentAcc(currentState)[2] * self.dt
        self.flightState.append(FlightState(x, y, z, v_x, v_y, v_z, currentState.t + self.dt))

    def getCurrentAcc(self, currentState):
        factor = self.getFactor(currentState)
        velocity = vector(currentState.v_x, currentState.v_y, currentState.v_z)
        speed = mag(velocity)
        a_airDrag = factor * (-B2m) * speed * velocity
        a_coriolis = 2 * cross(velocity, selfRotation)
        a = a_airDrag + a_coriolis + g
        currentAcc = [a.x, a.y, a.z]
        return currentAcc

    def getFactor(self, currentState):
        alpha = 2.5
        a = 6.5e-3
        factor = 0
        try:
            factor = (1 - a * currentState.y / 288.15)**alpha
        except ValueError:
            pass
        return factor


def calculate(target):
    initSpeed_x = initSpeed * math.sin(theta) * cosf
    initSpeed_y = initSpeed * math.cos(theta)
    initSpeed_z = initSpeed * math.sin(theta) * sinf
    initState = FlightState(0., 0., 0., initSpeed_x, initSpeed_y, initSpeed_z)
    cannonShell = CannonShell(initState, 0.1)
    while True:
        if cannonShell.flightState[-1].y < target[1] and cannonShell.flightState[-1].v_y < 0:
            finalState = cannonShell.flightState[-1]
            for i in range(5):  # 5 times Newton-Cotes
                dv = math.sqrt(finalState.v_x**2 + finalState.v_y**2 + finalState.v_z**2)
                d = (finalState.y - target[1]) * dv / finalState.v_y
                finalState.x -= d * finalState.v_x / dv
                finalState.y -= d * finalState.v_y / dv
                finalState.z -= d * finalState.v_z / dv
            break
        cannonShell.getNextState()
    return cannonShell


def aim_coarse(target):
    global sign, theta, initSpeed, farthest_d
    while True:
        cannonShell = calculate(target)
        d = math.sqrt(cannonShell.flightState[-1].x**2 + cannonShell.flightState[-1].z**2)
        if sign == 1:
            if farthest_d <= d:
                farthest_d = d
                theta += math.pi / (2 * 300)       
            else:
                sign = 2
        elif sign == 2:
            accuracy = d - math.sqrt(target[0]**2 + target[2]**2)
            if math.fabs(accuracy) < hit_area:
                break
            initSpeed -= accuracy / 1000


def aim_find(target):
    global sign, theta, sinf, cosf, initSpeed, farthest_d
    tmp_num = 30
    pre_accuracy_v = tmp_num
    while True:
        cannonShell = calculate(target)
        accuracy_v = math.fabs(cannonShell.flightState[-1].x / cannonShell.flightState[-1].z - target[0] / target[2])
        d = math.sqrt(cannonShell.flightState[-1].x**2 + cannonShell.flightState[-1].z**2)
        if sign == 1 or sign == 2:
            if accuracy_v < pre_accuracy_v and sign == 2 or accuracy_v > pre_accuracy_v and sign == 1:
                sign = 2
                sinf -= accuracy_v / tmp_num
                cosf = math.sqrt(1 - sinf**2)
            elif accuracy_v < pre_accuracy_v and sign == 1 or accuracy_v > pre_accuracy_v and sign == 2:
                sign = 1
                sinf += accuracy_v / tmp_num
                cosf = math.sqrt(1 - sinf**2)
            if math.fabs(pre_accuracy_v - accuracy_v) < 1e-5:
                sign = 0
            else:
                pre_accuracy_v = accuracy_v
        else:
            accuracy = d - math.sqrt(target[0]**2 + target[2]**2)
            if math.fabs(accuracy) < hit_area / 10:
                break
            initSpeed -= accuracy / tmp_num / 10
            


def updatePositon(objects, dt):

    def addForce(object, factor, dt, B2m = 4e-5):
        speed = mag(object.velocity)
        a_airDrag  = factor * (-B2m) * speed * object.velocity
        a_coriolis = 2 * cross(object.velocity, selfRotation)
        a = a_airDrag + a_coriolis + g
        object.velocity += a * dt

    def getFactor(object):
        alpha = 2.5
        a = 6.5e-3
        factor = 0
        try:
            factor = (1 - a * object.pos.y / 288.15)**alpha
        except ValueError:
            pass
        return factor

    for object in objects:
        factor = getFactor(object)
        object.pos = object.pos + object.velocity * dt
        addForce(object, factor, dt)


def shoot(object):
    print "theta: ", theta * 180 / math.pi
    print "initSpeed: ", initSpeed
    initSpeed_x = initSpeed * math.sin(theta) * cosf
    initSpeed_y = initSpeed * math.cos(theta)
    initSpeed_z = initSpeed * math.sin(theta) * sinf
    object.velocity = vector(initSpeed_x, initSpeed_y, initSpeed_z)
    deltat = 0.1
    scene.center = targetPlane.pos
    scene.forward = (-1, 0, 0)
    storeData(target, object)
    while True:
        rate(100)
        object.trail.append(pos=object.pos)
        updatePositon([object], deltat)
        if object.pos.y < -1000:
            print object.pos
            del object


def storeData(target, object):
    f = open("shootParadise.txt", "w")
    print >> f, "Target position:\n\tX: %f \n\tY: %f \n\tZ: %f\n" % (target[0], target[1], target[2])
    print >> f, "Shooting Velocity: %f\t%f\t%f\n" % (object.velocity.x, object.velocity.y, object.velocity.z)
    f.close()


shell = sphere(pos=(0,0,0), radius=1, color=color.cyan)
shell.trail = curve(color=shell.color)
battery = box(pos=(0,-1.1,0), size=(10,0.2,10), color=color.green)
targetPlane = box(pos=tuple(target), size=(20,0.2,20), color=color.green)
axis_x = arrow(pos=(0,0,0), axis=(50000,0,0), shaftwidth=0.1, color=color.blue)
axis_y = arrow(pos=(0,0,0), axis=(0,50000,0), shaftwidth=0.1, color=color.blue)
axis_z = arrow(pos=(0,0,0), axis=(0,0,50000), shaftwidth=0.1, color=color.blue)

aim_coarse(target)
aim_find(target)
shoot(shell)
