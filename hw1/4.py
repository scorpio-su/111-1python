import turtle

#make circle
list1 = ['blue', 'red', 'green']
turtle.showturtle()
turtle.color(list1[0])
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)

#make number
turtle.color(list1[1])
turtle.penup()
turtle.goto(90,-5)
turtle.pendown()
turtle.write("3",align= "center")
turtle.penup()
turtle.goto(-90,-5)
turtle.pendown()
turtle.write("9", align= "center")
turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.write("12",align= "center")
turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
turtle.write("6",align= "center")

#hour and minute hands
turtle.color(list1[2])
turtle.width(2)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.forward(70)

turtle.width(3)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.left(172.5)
turtle.forward(70)

turtle.done()
