"This code refers to picture #3 in the pdf"
import itertools
def f(d,c):
    a = (d**2) + c
    return a
x=[]
y=[]
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = -0.5475+(i/(50**3))
    b = 0.56376+(k/(50**3))
"we managed to find a point closer to the edge of the set by using the mouse"
"to hover over our plot and looking at the co-ordinates, so that when we zoomed"
"in we would get a more interesting plot."
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
import matplotlib.pylab as plt
plt.plot(x, y, color='black', marker='o', linewidth=0, markersize=1)
plt.axis("equal")
"we made the axis equal so that the plot would look true to the mandelbrot set"
"and it wouldn't be stretched"
plt.savefig("Mandelbrot Set Black zoom 2.png")
plt.show()
