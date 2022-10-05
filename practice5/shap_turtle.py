import turtle as t
import random as rnd

num = int(input("Enter Your Shape sides number: "))
color = input("Enter Your desired color: ")

t.colormode(255)
t.title("Shapes")
t.speed(4)
t.color("blue")
t.shape("circle")
t.shapesize(0.001,0.001,0.001)
t.pensize(10)
t.pencolor(color)
t.fillcolor(color)

t.begin_fill()
for i in range(num):
    t.bgcolor(rnd.randint(0 , 255) , rnd.randint(0 , 255) , rnd.randint(0 , 255))
    t.forward(100)
    t.left(360/num)
t.end_fill()
t.mainloop()
#----------------------------------------------------------------------
# import turtle
# poly = turtle.Turtle()
# sides = int(input('Enter the number of sides: '))
# while True:
#     color = input('Enter the color(red, blue, green, yellow, black, purple): ')
#     if color == 'red' or color == 'blue' or color == 'green' or color == 'yellow' or color == 'black' or color == 'purple' :
#         poly.color(color)
#         break
#     else:
#         print('you have to choose between "red", "blue", "green" or "yellow" or "black" or "Purple" ')
#         continue
# for i in range(sides):
#     poly.forward(180)
#     poly.right(360 / sides)
# turtle.done()
