import turtle as t
import random
t.shape("turtle")
t.speed(0)
t.pensize(3)
t.up()
t.goto(-250,250)
t.down()
for x in range(4):     #먼저 사각형을 그립니다.
    t.fd(500)
    t.rt(90)
t.up()
t.circle(10)     #거북이를 별모양 안으로 집어넣는 장애물입니다.
t.home()     #거북이를 원위치 시킵니다.
t.up()
t.goto(-125,125)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.write("함!!정",False,"center",("",15))     #함정이란 글자를 표시하였습니다.
t.up()
t.home()
t.setheading(90)
for x in range(250): #(0,250)까지 거북이를 이동시킵니다.
    t.fd(1)
t.down()
t.color("red") 
t.setheading(250)     #초기 설정 각도를 250도로 합니다.
while t.ycor() > -250:     
    t.fd(1)
    
t.setheading(38)      #벽에 부딪혀 팅겨 보이는 효과를 줍니다.
t.color("orange")
while t.xcor() < 250:     #사각형 밖을 넘어가지 않도록 설정을 하였습니다.
    t.fd(1)
t.color("yellow")
t.setheading(180)     #벽에 부딪혀 팅겨 보이는 효과를 줍니다.
for x in range(500):
    t.fd(1)
t.setheading(322)
t.color("green")
while t.ycor() > -250:
    t.fd(1)
t.setheading(110)
t.color("blue")
while t.ycor()<250:
    t.fd(1)
t.up()
t.lt(115)
for x in range(91):
    t.fd(2)
t.goto(0,84)     #     거북이가 장애물에 걸려 별모양 안으로 들어옵니다.
t.setheading(250)
t.down()
for x in range(158):
    t.fd(1)
t.setheading(38)
t.color("green")
for x in range(162):
    t.fd(1)
t.setheading(180)
t.color("yellow")
for x in range(153):
    t.fd(1)
t.setheading(322)
t.color("orange")
for x in range(164):
    t.fd(1)
t.setheading(108)
t.color("red")
for x in range(160):
    t.fd(1)
