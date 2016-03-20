# programming to solve population model and provide a diagrammatic analysis
# written by whuCanon, last modified on 2016/03/19

from pylab import *
import math

frequency = 10000    # larger the value, preciser the result
a = 0.               # the paradise a
b = 0.               # the paradise b
N = []               # the list of number of population
t = [0]              # the list of time moment

# receive input paradise and calculate a suitable end time
while True:
    try:
        a = float(raw_input("Please enter the parameter_a (best in 0.01-100):"))
        b = float(raw_input("Please enter the parameter_b (best in 0-10):"))
        N.append(int(raw_input("Please enter the initial N:")))
        if a / b > N[0]:
            end_t = (math.log(a / b) / a) * 3
        else:
            end_t = 1 / (a + 1/ N[0]) / b
        if math.fabs(a/b - N[0]) < 10:
            end_t *= 2
        DET_T = end_t / frequency
        break
    except ValueError:
        print "Please enter a right number!"

# calculate the N every moment
for i in range(int(end_t / DET_T)):
    tmp_N = N[i] + (a * N[i] - b * N[i]**2) * DET_T
    N.append(tmp_N)
    t.append((i + 1) * DET_T)

# get the minimal and maximal t and N
xmin, xmax = min(t), max(t)
ymin, ymax = int(min(N)), round(max(N))

# adjust the diagram
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + 2 * dy)

# adjust the axis
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# add label
xticks([xmin, xmax])
yticks([ymin, ymax/2, ymax],[ymin, ymax/2, ymax])

# add auxiliary line
t_p = ymax / 2    # turning point
plot([0,xmax],[t_p,t_p], color='red', linewidth=2.5, linestyle="--")
plot([0,xmax],[ymax,ymax], color='red', linewidth=2.5, linestyle="--")

# name the axis
xlabel('time/year')
ylabel('population')

# plot and save
plot(t, N, label="population growth")
legend(loc='upper center')
savefig("population_model_2.png",dpi=256)
show()
