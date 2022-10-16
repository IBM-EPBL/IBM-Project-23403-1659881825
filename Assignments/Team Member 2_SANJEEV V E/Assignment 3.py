import turtle
import time
wn= turtle.getscreen()
wn.bgcolor("yellow")

#gui interfrace
pen= turtle.Turtle()
pen.color("blue")
pen.width(6)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)



#red light
red_light =turtle.Turtle()
red_light.shape("circle")
red_light.color("white")
red_light.penup()
red_light.goto(0, 40)

#orange light
orange_light =turtle.Turtle()
orange_light.shape("circle")
orange_light.color("white")
orange_light.penup()
orange_light.goto(0, 0)

#Green light
green_light =turtle.Turtle()
green_light.shape("circle")
green_light.color("white")
green_light.penup()
green_light.goto(0, -40)


while True:
    green_light.color("white")
    red_light.color("red")
    print("Red light Blinked ")
    print("Blink!!")
    time.sleep(3)
    print("Blink!!")

    red_light.color("white")
    orange_light.color("orange")
    green_light.color("white")
    print("Yellow light Blinked")
    print("Blink!!")
    time.sleep(3)
    print("Blink!!")
    
    red_light.color("white")
    orange_light.color("white")
    green_light.color("green")
    print("Green light on")
    print("Blink!!")
    time.sleep(2)
    print("Blink!!")


wn.mainloop()
