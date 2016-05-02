# a simple program to analyse billiard problem on some different table
# written by whuCanon, last modified on 2016/05/2

import sys
import math
import time
from visual import *
from matplotlib import pyplot


alpha = 0.
ball_initPos = (100,100,0)
ball_initVel = vector(80,33,-0)


table = [box(pos=( 200,0,0), length=1,height=400,width=1, color=color.white),\
         box(pos=(-200,0,0), length=1,height=400,width=1, color=color.white),\
         box(pos=( 0,200,0), length=400,height=1,width=1, color=color.white),\
         box(pos=(0,-200,0), length=400,height=1,width=1, color=color.white)]
wall_1 = sphere(pos=(0-alpha,0,0), radius=50, color=color.red)
wall_2 = box(pos=(0,0,0),length=2*alpha, height=100, width=1, color=color.red)
wall_3 = sphere(pos=(0+alpha,0,0), radius=50, color=color.red)
ball = sphere(pos=ball_initPos, radius=1, color=color.green)
ball.trail = curve(color=ball.color)
ball.velocity = ball_initVel


fig = pyplot.figure(figsize=(12,12))
max_x, max_vx = table[0].pos.x, math.sqrt(ball_initVel.x**2 + ball_initVel.y**2)
ax = fig.add_subplot(111, xlim=(-max_x,max_x), ylim=(0,max_vx), autoscale_on=False)
ax.set_title(r"Billiard: $\alpha = $" + str(alpha))
ax.set_xlabel(r'$x$', fontsize=16)
ax.set_ylabel(r'$v_x$', fontsize=16)
x, y = [], []

pre_x, pre_y = ball_initPos[0], ball_initPos[1]
if ball_initPos[1] <= 0:
    sign = 0
else:
    sign = 1


def collided_wall_2(pos):
    if pos.y >= wall_2.height/2 or pos.y <= -wall_2.height/2:
        return False
    if pos.x >= wall_2.length/2 or pos.x <= -wall_2.length/2:
        return False
    return True


def collided_wall(obj, pos):
    if mag(pos-wall_1.pos) <= wall_1.radius or mag(pos-wall_3.pos) <= wall_3.radius:
        return True
    if collided_wall_2(pos):
        return True
    if pos.x >= table[0].pos.x:
        obj.pos.x = 2 * table[0].pos.x - pos.x
        obj.velocity.x = -obj.velocity.x
    if pos.x <= table[1].pos.x:
        obj.pos.x = 2 * table[1].pos.x - pos.x
        obj.velocity.x = -obj.velocity.x
    if pos.y >= table[2].pos.y:
        obj.pos.y = 2 * table[2].pos.y - pos.y
        obj.velocity.y = -obj.velocity.y
    if pos.y <= table[3].pos.y:
        obj.pos.y = 2 * table[2].pos.y - pos.y
        obj.velocity.y = -obj.velocity.y
    return False
    

def fixCollision(obj, pos):
    sign = 0
    if mag(pos-wall_1.pos) <= wall_1.radius:
        high, low = obj.pos, pos
        for i in range(10):
            tmp = (high + low) / 2
            if mag(tmp-wall_1.pos) <= wall_1.radius:
                low = tmp
            else:
                high = tmp
        if mag(tmp-wall_3.pos) >= wall_3.radius:
            intsecPoint = tmp
            sign = 1
    if sign != 1 and mag(pos-wall_3.pos) <= wall_3.radius:
        high, low = obj.pos, pos
        for i in range(10):
            tmp = (high + low) / 2
            if mag(tmp-wall_1.pos) <= wall_1.radius:
                low = tmp
            else:
                high = tmp
        intsecPoint = tmp
        sign = 3

    if collided_wall_2(pos):
        high, low = obj.pos, pos
        for i in range(10):
            tmp = (high + low) / 2
            if collided_wall_2(tmp):
                low = tmp
            else:
                high = tmp
        if math.fabs(math.fabs(tmp.y)-wall_2.height/2) < math.fabs(math.fabs(tmp.x)-wall_2.length/2):
            intsecPoint = tmp
            sign = 2

    if sign == 1:
        wall_o = wall_1.pos
    elif sign == 2:
        
        if tmp.y > 0:
            obj.pos.y =  wall_2.height - pos.y
        else:
            obj.pos.y = -wall_2.height - pos.y
        obj.velocity.y = -obj.velocity.y
        return
    elif sign == 3:
        wall_o = wall_3.pos
    else:
        return

    tmp_vec = norm(intsecPoint-wall_o)
    tmp_vBall = norm(obj.velocity)
    tmp_dis1 = mag(pos-intsecPoint)
    tmp_dis2 = -2 * tmp_dis1 * dot(tmp_vBall,tmp_vec)

    obj.pos = pos + tmp_dis2 * tmp_vec
    obj.velocity = mag(obj.velocity) * norm(tmp_dis1 * tmp_vBall + tmp_dis2 * tmp_vec)


def updatePositon(obj, dt = 0.01):
    global pre_x, pre_y
    pre_x, pre_y = obj.pos.x, obj.pos.y
    tmp_pos = obj.pos + obj.velocity * dt
    if collided_wall(obj, tmp_pos):
        fixCollision(obj, tmp_pos)
    else:
        obj.pos = tmp_pos


def getSpecialPoint(obj):
    global x, y
    if sign == 0 and obj.pos.y > 0 or sign == 1 and obj.pos.y < 0:
        x.append(pre_x - (obj.pos.x-pre_x) * pre_y/obj.pos.y)
        y.append(obj.velocity.x)



for i in range(2000000):
    rate(1000)
    # ball.trail.append(pos=ball.pos)
    updatePositon(ball)
    getSpecialPoint(ball)

pyplot.scatter(x, y)
pyplot.savefig("billiard_squareTable.png",dpi=72)
pyplot.show()