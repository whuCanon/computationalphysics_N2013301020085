import math
from visual import *

k = 1.
m_J = 100.
m_S = m_J * k
d_SJ = 100.

jupiter = sphere(pos=(d_SJ*m_S/(m_J+m_S),0,0), radius=5, color=color.cyan, opacity=0.8, material=materials.wood)
sun   = sphere(pos=(-d_SJ*m_J/(m_J+m_S),0,0), radius=10, color=color.yellow, material=materials.emissive)
earth = sphere(pos=((jupiter.pos.x+4.2*sun.pos.x)/5.2,0,0), radius=2, material=materials.earth)
jupiter.velocity = vector(0,k*math.sqrt(m_J/(k+1)/d_SJ),0)
sun.velocity = vector(0,-math.sqrt(m_J/(k+1)/d_SJ),0)
earth.velocity = 2.3 * jupiter.velocity
both_vec = (k*sun.velocity + jupiter.velocity) / (1 + k)
jupiter.velocity -= both_vec
sun.velocity -= both_vec
jupiter.trail = curve(color=jupiter.color)
sun.trail = curve(color=sun.color)
earth.trail = curve(color=earth.color)


def updatePosition(dt = 0.1):
    d_SJ = mag(jupiter.pos - sun.pos)
    d_SE = mag(earth.pos - sun.pos)
    d_JE = mag(earth.pos - jupiter.pos)
    #jupiter.velocity -= jupiter.pos * (4*math.pi**2/d_SJ**3) * dt
    jupiter.velocity += norm(sun.pos-jupiter.pos) * m_S/d_SJ**2 * dt
    #sun.velocity -= sun.pos * (4*math.pi**2/d_SJ**3) * dt
    sun.velocity += norm(jupiter.pos-sun.pos) * m_J/d_SJ**2 * dt
    earth.velocity += norm(sun.pos-earth.pos) * m_S/d_SE**2 * dt
    earth.velocity += norm(jupiter.pos-earth.pos) * m_J/d_JE**2 * dt
    jupiter.pos += jupiter.velocity * dt
    sun.pos += sun.velocity * dt
    earth.pos += earth.velocity * dt


while True:
    rate(1000)
    jupiter.trail.append(pos=jupiter.pos)
    sun.trail.append(pos=sun.pos)
    earth.trail.append(pos=earth.pos)
    updatePosition()