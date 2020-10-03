"This code refers to picture #1 in the pdf"
import itertools
"itertool was used for the product function, allowing us to quickly go through"
"many real and imaginary values. This was faster and more efficient than using"
"for loops"
def f(d,c):
    a = (d**2) + c
    return a
"I used this function to define the mandelbrot set"
x=[]
y=[]
for i,k in itertools.product(range(-100,101),range(-100,101)):
    a = i/50
    b = k/50
"this will itterate a and b through the range -2,2 in intervals of 1/50."
"this worked well as we know any values with a modulus over 2 would diverge"
    itters = 0
    r = complex(a,b)
    z = 0
"we found that 200 itterations was both fast and produced an accurate looking"
"mandelbrot set."
    while itters < 200:
        try:
            z = f(z,r)
            itters += 1
        except OverflowError:
            break
"we had to ignore OverflowErrors as these were an issue when we ran our code."
"We found that when we broke every time we got one of these errors, the code"
"worked fine"
    if abs(z) < 2:
        x.append(a)
        y.append(b)
import matplotlib.pylab as plt
plt.plot(x, y, color='black', marker='o', linewidth=0, markersize=1)
plt.axis("equal")
plt.savefig("Mandelbrot Set Black.png")
plt.show()
