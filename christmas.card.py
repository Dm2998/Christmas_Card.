import turtle
import random

def drawHat():
    pen.color('red')
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(3):
        pen.fd(50)
        pen.right(120)
    pen.end_fill()
    for i in range(6):
        pen.dot(10,'white')
        pen.fd(10)
    pen.right(130)
    pen.fd(55)
    pen.dot(10,'white')

def makeSnow():
    for i in range(50):
        snow=turtle.Turtle()
        snow.pu()
        snow.color("white")
        snow.shape("circle")
        snow.speed(0)
        snow.goto(random.randint(-700,700),random.randint(-700,700))
        snow.dot(7,'white')
        snowlist.append(snow)

def snowfall():
    for i in snowlist:
        i.goto(random.randint(-700,700),random.randint(-700,700))
        i.dot(7,'white')

card=turtle.Screen()
card.setup(1.0,1.0,0,0)
card.title("Christmas Greetings!")

colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
card.bgcolor(random.choice(colors))

tree=turtle.Turtle()
tree.color("green")


tree.pu()
tree.goto(100,0)  

pen=turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.pu()
pen.setx(-500)

pen.write("Merry\nChristmas!!\nDiego",font=("ravie",40,"italic"),align="left")
pen.setheading(-90)
pen.fd(100)
pen.write("TO ALL OF YOU",font=("Courier",30,"bold"),align="left")

pen.setheading(0)
pen.fd(360)
pen.left(145)
pen.fd(40)
drawHat()

card.tracer(False)
snowlist=[]
makeSnow()
card.tracer(True)
while True:
    snowfall()
    card.update()


turtle.done()

