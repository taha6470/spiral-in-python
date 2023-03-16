import turtle as t
import random
t.colormode(255)
def set_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
timmy=t.Turtle()
for i in range(50):
    timmy.circle(45)
    timmy.color(set_color())
    timmy.right(10)