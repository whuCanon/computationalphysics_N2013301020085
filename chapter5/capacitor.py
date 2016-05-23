import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import pyplot
from matplotlib import numpy


X = numpy.arange(-1, 1, 0.05)
Y = numpy.arange(-1, 1, 0.05)
V = []
detV = 10000
end_detV = 1e-5 * len(X)


def update_V():
    global detV
    detV = 0
    for i in xrange(1, len(X) - 1):
        for j in xrange(1, len(Y) - 1):
            if (i==len(X)/3 or i==len(X)*2/3) and len(Y)/3<j<len(Y)*2/3:
                continue
            tmp = (V[i-1][j] + V[i+1][j] + V[i][j-1] + V[i][j+1]) / 4
            detV += numpy.abs(tmp - V[i][j])
            V[i][j] = tmp


# initialize V
V.append([0. for i in xrange(len(X))])
for i in xrange(1, len(X) - 1):
    tmp = [0.]
    for j in range(1, len(Y) - 1):
        if i==len(X)/3 and len(Y)/3<j<len(Y)*2/3:
            tmp.append(1.)
        elif i==len(X)*2/3 and len(Y)/3<j<len(Y)*2/3:
            tmp.append(-1.)
        else:
            tmp.append(0.)
    tmp.append(0.)
    V.append(tmp)
V.append([0. for i in xrange(len(X))])

while detV > end_detV:
    update_V()

X, Y = numpy.meshgrid(X, Y)

fig = pyplot.figure()
ax = fig.gca(projection='3d')
ax.set_title(r"Electric potential near two metal plates")
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$V$')
surf = ax.plot_surface(X, Y, V, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
pyplot.show()
