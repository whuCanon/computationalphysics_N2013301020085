
import sys
import math
import pickle
import random

HEIGHT = 8
WIDTH  = 5

s = []
sweep = 5

Jfile = open("J.pkl", 'r')
J = pickle.load(Jfile)

def initState(s):
    for i in range(HEIGHT):
        tmp = []
        for j in range(WIDTH):
            tmp.append(-1.)
        s.append(tmp)


def calEflip(s, row, col):
    E = 0.
    for i in xrange(HEIGHT):
        for j in xrange(WIDTH):
            E -= J[row*WIDTH+col][i*WIDTH+j] * s[row][col] * s[i][j]
    return -2*E


def match(s):
    for i in xrange(sweep):
        for row in xrange(HEIGHT):
            for col in xrange(WIDTH):
                eflip = calEflip(s, row, col)
                if eflip < 0:
                    s[row][col] = -s[row][col]
                elif random.random() < 0.1:
                    s[row][col] = -s[row][col]


def display(s):
    for i in xrange(HEIGHT):
        for j in xrange(WIDTH):
            if int(s[i][j]) == 1:
                sys.stdout.write("+ ")
            else:
                sys.stdout.write("  ")
        print ""


initState(s)
s[0] = [ 1, 1, 1, 1, 1]
s[1] = [-1,-1,-1, 1,-1]
s[2] = [-1,-1, 1,-1,-1]
s[3] = [-1, 1,-1,-1,-1]
s[4] = [ 1,-1,-1,-1,-1]
s[5] = [ 1,-1,-1,-1, 1]
s[6] = [-1, 1, 1, 1,-1]
s[7] = [-1,-1,-1,-1,-1]
match(s)
display(s)