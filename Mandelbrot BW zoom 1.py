"This code refers to picture #2 in the pdf"
import itertools
def f(d,c):
    a = (d**2) + c
    return a
x=[]
y=[]
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = -0.53+(i/(50**2))
    b = 0.57+(k/(50**2))
"For the black and white plots, we used the graph plotted in the first code"
"to find a point on the edge of the set that would be interesting to zoom in on"
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 130:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break            
    if abs(z) < 2:
        x.append(a)
        y.append(b)
"this code ensured that any points that do not exceed 2 after 130 itterations"
"would be plotted as a black point. This meant that all points that converge"
"would certainly be plotted in black."
import matplotlib.pylab as plt
"matplotlib was imported further down so that the code was sectioned so that"
"all code close to each other would be relevant to that section"
plt.plot(x, y, color='black', marker='o', linewidth=0, markersize=1)
plt.axis("equal")
plt.savefig("Mandelbrot Set Black zoom 1")
plt.show()
