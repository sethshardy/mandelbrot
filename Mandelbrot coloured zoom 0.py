"This code refers to picture #5 in the pdf"
import itertools
def f(d,c):
    a = (d**2) + c
    return a
"This is the function that defines the mandelbrot set"
"We wrote it in this form so that we didn't have to itterate from 0"
"This meant we could see what happened to numbers further down the line"
"without starting at 0, however, we did not have to use this in my project."
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
"These lists would determine the points that divereged at different speeds"
"as we were given that any number with a modulus greater than 2 would diverge"
"we could look at how many itterations it took to become greater than 2"
"then we could colour these points differently on how many itterations it took"
"for the modulus to exceed 2"
"We decided to use 4 lists for points that diverged at different speeds so that"
"when we plotted the diagram we would have a smoother gradient, the plot"
"would look better and contain more information"
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = i/50
    b = k/50
"to zoom in, we made the /50 into /(50^2) so that we would be considerring"
"points with a smaller range, which acted the same as zooming in. We chose"
"a co-ordinatre to zoom in at by zooming in on the website tilde.club/~david/m/"
"we found that the point -0.54746+0.56390i was a good point as it was precise"
"and it was on the very edge of the set, so it woukd be an interesting point"
"to zoom in on"
    itters = 0
    r = complex(a,b)
    z = 0
    while itters < 130 and abs(z) < 2:
        try:
            z = f(z,r)
            itters += 1
"We found that we got an OverflowError when the itterations was above a certain"
"amount, so we used the try and except loops to stop this. Once we added these"
"the code worked fine"
        except OverflowError:
            break
"We used 130 itterations as this was a substantial amount that did not take"
"a long time to run. It was a good number as later on it gave us a lot of room"
"to increase the range of itterations it took to diverge. For example, it meant"
"that when we zoomed in we could take the vslow list to be points that took"
"over 100 itterations to diverge"
    if 20 < itters <= 129:
        vslowx.append(a)
        vslowy.append(b)
    if 10 < itters <= 20:
        slowx.append(a)
        slowy.append(b)
    if 5 < itters <= 10:
        medx.append(a)
        medy.append(b)
    if 0 < itters <= 5:
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
"To decide on what colour to use for each list of points, we searched up a"
"colour hex chart and chose red points in a gradient getting gradually darker"
"We thought that this would look good as it would represent the gradient of"
"how many itterations it took for a number to diverge and have a modulus"
"that was greater than 2"
plt.axis("equal")
plt.savefig("Mandelbrot #7.png")
plt.show()
