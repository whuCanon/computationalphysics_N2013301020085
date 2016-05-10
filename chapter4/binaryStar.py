import math
from visual import *

k = 1.
m = 100
M = m * k
d = 100.

earth = sphere(pos=( d*M/(m+M),0,0), radius=5, color=color.white, material=materials.earth)
sun   = sphere(pos=(-d*m/(m+M),0,0), radius=10, color=color.yellow, material=materials.emissive)
earth.velocity = vector(0,k*math.sqrt(m/(k+1)/d)/3,0)
sun.velocity = vector(0,-math.sqrt(m/(k+1)/d),0)
both_vec = (k*sun.velocity + earth.velocity) / (1 + k)
earth.velocity -= both_vec
sun.velocity -= both_vec
earth.trail = curve(color=earth.color)
sun.trail = curve(color=sun.color)


def updatePosition(earth, sun, dt = 0.1):
    d = mag(earth.pos - sun.pos)
    #earth.velocity -= earth.pos * (4*math.pi**2/d**3) * dt
    earth.velocity += norm(sun.pos-earth.pos) * k*m/d**2 * dt
    #sun.velocity -= sun.pos * (4*math.pi**2/d**3) * dt
    sun.velocity += norm(earth.pos-sun.pos) * m/d**2 * dt
    earth.pos += earth.velocity * dt
    sun.pos += sun.velocity * dt


while True:
    rate(2000)
    earth.trail.append(pos=earth.pos)
    sun.trail.append(pos=sun.pos)
    updatePosition(earth, sun)