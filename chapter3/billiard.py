# a simple program to analyse billiard problem on some different table
# written by whuCanon, last modified on 2016/04/30

import sys
import math
import time
from visual import *
from matplotlib import pyplot


alpha = 0
ball_initPos = (200,200,200)
ball_initVel = vector(-20,-2,-10)


table = [box(pos=( 200,0,0), length=1,height=200,width=200, color=color.white),\
         box(pos=(-200,0,0), length=1,height=200,width=200, color=color.white),\
         box(pos=( 0,200,0), length=200,height=1,width=200, color=color.white),\
         box(pos=(0,-200,0), length=200,height=1,width=200, color=color.white),\
         box(pos=(0,0,-200), length=200,height=200,width=1, color=color.white),]
wall_1 = sphere(pos=(0-alpha,0,0), radius=30, color=color.red)
wall_2 = box(pos=(0,0,0),length=alpha, height=60, width=60, color=color.red)
wall_3 = sphere(pos=(0+alpha,0,0), radius=30, color=color.red)
ball = sphere(pos=ball_initPos, radius=1, color=color.green)
ball.velocity = ball_initVel


def collided_wall_2(pos):
    if pos.y >= wall_2.height or pos.y <= -wall_2.height:
        return False
    if pos.z >= wall_2.width  or pos.z <= -wall_2.width:
        return False
    if pos.x >= wall_2.length or pos.x <= -wall_2.length:
        return False
    return True


def collided_wall(obj, pos):
    if mag(pos-wall_1.pos) <= wall_1.radius or mag(pos-wall_3.pos) <= wall_3.radius:
        return True
    if collided_wall_2(pos):
        return True
    if pos.x >= table[0].pos.x:
        obj.pos.x = 2 * table[0].pos.x - pos.x
    if pos.x <= table[1].pos.x:
        obj.pos.x = 2 * table[1].pos.x - pos.x
    if pos.y >= table[2].pos.y:
        obj.pos.y = 2 * table[2].pos.y - pos.y
    if pos.y <= table[3].pos.y:
        obj.pos.y = 2 * table[2].pos.y - pos.y
    if pos.z >= -table[4].pos.z:
        obj.pos.z = -2 * table[4].pos.z - pos.z
    if pos.z <= table[4].pos.z:
        obj.pos.z = 2 * table[4].pos.z - pos.z
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
    if sign != 1:
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
        if tmp.y > 0 and math.fabs(tmp.y-wall_2.height) > math.fabs(tmp.x-wa):
            intsecPoint = tmp
            sign = 2



def updatePositon(obj, dt = 0.01):
    tmp_pos = obj.pos + obj.velocity * dt
    if collided_wall(obj, tmp_pos):
        obj.pos, obj.velocity = fixCollision(obj, tmp_pos)