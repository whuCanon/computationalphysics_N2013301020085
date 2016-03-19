# programming to solve population model and provide a diagrammatic analysis
# written by whuCanon, last modified on 2016/03/19

from pylab import *
import math

DET_T = 0.01
a = 0.
b = 0.
end_t = 0
N = []
t = [0]

while True:
	try:
		a = float(raw_input("Please enter the parameter_a (best in 0.01-100):"))
		b = float(raw_input("Please enter the parameter_b (best in 0-10):"))
		N.append(int(raw_input("Please enter the initial N:")))
		if a / b > N[0]:
			end_t = (math.log(a / b) / a) * 3
		else:
			end_t = 1 / (a + 1/ N[0]) / b
			DET_T = 0.0000001
		break
	except ValueError:
		print "Please enter a right number!"

for i in range(int(end_t / DET_T)):
	tmp_N = N[i] + (a * N[i] - b * N[i]**2) * DET_T
	N.append(tmp_N)
	t.append((i + 1) * DET_T)

xmin, xmax = min(t), max(t)
ymin, ymax = int(min(N)), int(round(max(N)))

dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + 2 * dy)

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

xticks([xmin, xmax])
yticks([ymin, ymax/2, ymax],[ymin, ymax/2, ymax])

t_p = ymax / 2	# turning point
plot([0,xmax],[t_p,t_p], color='red', linewidth=2.5, linestyle="--")
plot([0,xmax],[ymax,ymax], color='red', linewidth=2.5, linestyle="--")

xlabel('time/year')
ylabel('population')

plot(t, N, label="population growth")
legend(loc='upper center')
savefig("exercice_2.png",dpi=256)
show()
