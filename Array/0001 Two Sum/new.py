import turtle
import math

# 创建一个画布和画笔
screen = turtle.Screen()
screen.title("动态爱心")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.width(2)

# 准备绘制爱心的函数
def draw_heart():
    pen.clear()
    pen.penup()
    pen.goto(0, 150)
    pen.pendown()
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2 * math.pi * 224 / 360)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2 * math.pi * 224 / 360)
    pen.forward(224)
    pen.end_fill()

# 让爱心动起来
angle = 0
while True:
    angle += 1
    pen.left(2)
    draw_heart()

# 点击画布关闭窗口
screen.mainloop()
