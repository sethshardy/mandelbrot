"This code refers to picture #8 in the pdf"
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
    a = -0.54746+(i/(50**4))
    b = 0.5639+(k/(50**4))
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 131 and abs(z) < 2:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break
    if 110 < itters <= 130:
        vslowx.append(a)
        vslowy.append(b)
    if 100 < itters <= 110:
        slowx.append(a)
        slowy.append(b)
    if 90 < itters <= 100:
        medx.append(a)
        medy.append(b)
    if 0 < itters <= 90:
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
plt.savefig("Mandelbrot coloured zoom 3.png")
plt.show()
