import turtle

list1 = ['red', 'green', 'yellow', 'blue']
turtle.showturtle()

#first circle
turtle.penup()
turtle.goto(-50,50)
turtle.pendown()
turtle.color(list1[0])
turtle.circle(50)

#second circle
turtle.penup()
turtle.goto(-50,-50)
turtle.pendown()
turtle.color(list1[1])
turtle.circle(50)

#third circle
turtle.penup()
turtle.goto(50,-50)
turtle.pendown()
turtle.color(list1[2])
turtle.circle(50)

#forth circle
turtle.penup()
turtle.goto(50,50)
turtle.pendown()
turtle.color(list1[3])
turtle.circle(50)

turtle.done()