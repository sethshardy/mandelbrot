"This code refers to picture #7 in the pdf"
import itertools
def f(d,c):
    a = (d**2) + c
    return a
x=[]
y=[]
fastx=[]
fasty=[]
medx=[]
medy=[]
slowx=[]
slowy=[]
vslowx=[]
vslowy=[]
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = -0.5475+(i/(50**3))
    b = 0.56376+(k/(50**3))
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 130 and abs(z) < 2:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break
    if 100 < itters <= 129:
        vslowx.append(a)
        vslowy.append(b)
"it took more itterations to clearly differentiate the different colours so"
"that they could be clearly seen on the diagram. We adjusted these accordingly"
"so that they looked good on each plot"
    if 70 < itters <= 100:
        slowx.append(a)
        slowy.append(b)
    if 40 < itters <= 70:
        medx.append(a)
        medy.append(b)
    if 0 < itters <= 40:
        fastx.append(a)
        fasty.append(b)
    if abs(z) < 2:
        x.append(a)
        y.append(b)
import matplotlib.pylab as plt
plt.plot(x, y, color='black', marker='o', linewidth=0, markersize=1)
plt.plot(vslowx, vslowy, color='#590000', marker='o', linewidth=0, markersize=1)
plt.plot(slowx, slowy, color='#8e0000', marker='o', linewidth=0, markersize=1)
plt.plot(medx, medy, color='#c60000', marker='o', linewidth=0, markersize=1)
plt.plot(fastx, fasty, color='#ff0000', marker='o', linewidth=0, markersize=1)
plt.axis("equal")
plt.savefig("Mandelbrot coloured zoom 2.png")
plt.show()
