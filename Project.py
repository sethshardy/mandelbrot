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
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = i/50
    b = k/50
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 100 and abs(z) < 2:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break
    if 20 < itters <= 30:
        slowx.append(a)
        slowy.append(b)
    if 10 < itters <= 20:
        medx.append(a)
        medy.append(b)
    if 0 < itters <= 10:
        fastx.append(a)
        fasty.append(b)
    if abs(z) < 2:
        x.append(a)
        y.append(b)
import matplotlib.pylab as plt
plt.plot(x, y, color='black', marker='o', linewidth=0, markersize=1)
plt.plot(slowx, slowy, color='yellow', marker='o', linewidth=0, markersize=1)
plt.plot(medx, medy, color='orange', marker='o', linewidth=0, markersize=1)
plt.plot(fastx, fasty, color='red', marker='o', linewidth=0, markersize=1)
plt.axis("equal")
plt.savefig("Mandelbrot #6.png")
plt.show()
