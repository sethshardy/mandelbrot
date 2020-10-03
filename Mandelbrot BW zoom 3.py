"This code refers to picture #4 in the pdf"
import itertools
def f(d,c):
    a = (d**2) + c
    return a
x=[]
y=[]
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = -0.54746+(i/(50**4))
    b = 0.5639+(k/(50**4))
"for this plot we kept everything the same from the 2nd zoom but"
"made the bottom 50^4 instead so that it would zoom in 50 times"
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
plt.savefig("Mandelbrot Set Black zoom 3.png")
plt.show()
