"This code refers to picture #6 in the pdf"
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
    a = -0.53+(i/(50**2))
    b = 0.57+(k/(50**2))
"We used the same points for each plot as the ones in the black and white"
"plot, so that we only needed to change the colours."
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 130 and abs(z) < 2:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break
    if 30 < itters <= 129:
        vslowx.append(a)
        vslowy.append(b)
    if 20 < itters <= 30:
        slowx.append(a)
        slowy.append(b)
    if 10 < itters <= 20:
        medx.append(a)
        medy.append(b)
    if 0 < itters <= 10:
        fastx.append(a)
        fasty.append(b)
"We increased the number of itterations it took for each colour so that when"
"we zoomed in, we could still differentiate points that took more or less"
"itterations to have their modulus exceeed 2 and subsequently diverge"
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
plt.savefig("Mandelbrot coloured zoom 1.png")
plt.show()
