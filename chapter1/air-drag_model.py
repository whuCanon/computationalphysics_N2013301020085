# a simple program to analyse air-drag model and provide a diagrammatic analysis
# written by whuCanon, last modified on 2016/03/24

from pylab import *
import math

frequency = 10000    # larger the value, preciser the result
a = 0.               # the paradise a
b = 0.               # the paradise b
v = []               # the list of velocity
t = [0]              # the list of time moment
real_v = []
sign = True

# receive input paradise and calculate a suitable end time
while True:
    try:
        a = float(raw_input("Please enter the parameter_a:"))
        b = float(raw_input("Please enter the parameter_b(upper zero):"))
        v.append(float(raw_input("Please enter the initial v:")))
        sign = a / b > v[0]
        end_t = log(10000) / b
        DET_T = end_t / frequency
        break
    except ValueError:
        print "Please enter a right number!"

# calculate the velocity every moment
for i in range(frequency):
    tmp_v = v[i] + (a - b * v[i]) * DET_T
    v.append(tmp_v)
    real_v.append((v[0] - a / b) * math.exp(-b*t[i]) + a / b)
    t.append((i + 1) * DET_T)
real_v.append((v[0] - a / b) * math.exp(-b*(t[frequency]+DET_T)) + a / b)

# get the minimal and maximal t and v
xmin, xmax = min(t), max(t)
if sign:
	ymin, ymax = v[0], a / b
else:
	ymax, ymin = v[0], a / b

# adjust the diagram
dy = (ymax - ymin) * 0.1
ylim(ymin, ymax + dy)

# add label
xticks([xmin, xmax])
yticks([ymin, ymax])

# add auxiliary line
plot([0,xmax],[ymax,ymax], color='red', linewidth=2.5, linestyle="--")

# name the axis
xlabel(r'$time/s$', fontsize=16)
ylabel(r'$v/m*s^{-1}$', fontsize=16)

# plot and save
plot(t, v, "blue", label="velocity numerical")
if sign:
	legend(loc='lower right')
else:
	legend(loc='upper right')

savefig("air-drag_model_2.png",dpi=256)
f = open("errorAnalysis_2.txt", "w")
f.write("numerical\t\treal\t\t\terror\n")
for i in range(frequency + 1):
	print >> f, "%f\t\t%f\t\t%e\n" % (v[i], real_v[i], v[i] - real_v[i])
print "the error analysis was stored"
f.close()
show()
