import turtle        # import turtle module
import random        # import random module

def drawHat():            # function to draw hat
    pen.color('red')        # set pen color to red
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(3):           # draw triangle  for hat  loop 3 times
        pen.fd(50)
        pen.right(120)
    pen.end_fill()
    for i in range(6):           # draw rectangle for hat loop 6 times
        pen.dot(10,'white')
        pen.fd(10)
    pen.right(130)
    pen.fd(55)
    pen.dot(10,'white')

def makeSnow():                     # function to make snow 
    for i in range(50):             # loop 50 times to make 50 snowflakes
        snow=turtle.Turtle()
        snow.pu()
        snow.color("white")
        snow.shape("circle")
        snow.speed(0)
        snow.goto(random.randint(-700,700),random.randint(-700,700))
        snow.dot(7,'white')
        snowlist.append(snow)

def snowfall():               # function to make snow fall   
    for i in snowlist:
        i.goto(random.randint(-700,700),random.randint(-700,700))
        i.dot(7,'white')

card=turtle.Screen()                 # create screen object for card
card.setup(1.0,1.0,0,0)               # set screen size to full screen
card.title("Christmas Greetings!")

colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
card.bgcolor(random.choice(colors))      # set background color to random color

tree=turtle.Turtle()
tree.color("green")


tree.pu()
tree.goto(100,0)  

pen=turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.pu()
pen.setx(-500)           # set pen to left side of screen

pen.write("Merry\nChristmas!!\nDiego",font=("ravie",40,"italic"),align="left")    # write Merry Christmas to card
pen.setheading(-90)
pen.fd(100)
pen.write("TO ALL OF YOU",font=("Courier",30,"bold"),align="left")    # write to all of you to card

pen.setheading(0)
pen.fd(360)
pen.left(145)
pen.fd(40)
drawHat()

card.tracer(False)
snowlist=[]
makeSnow()
card.tracer(True)
while True:                                 # loop to make snow fall
    snowfall()
    card.update()


turtle.done()             #closes it

