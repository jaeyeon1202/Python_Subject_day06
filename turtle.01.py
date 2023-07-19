import turtle
turtle.shape("turtle")

bang=int(input("방향:"))
length=int(input("길이:"))
if bang==1:
    turtle.pencolor("red")
    turtle.forward(length)
elif bang==2:
    turtle.pencolor("blue")
    turtle.right(90)
    turtle.forward(length)
turtle.done()