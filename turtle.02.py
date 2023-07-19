import turtle
turtle.shape("turtle")

a=input("도형종류:")

if a=="삼각형":
    length=int(input("한 변의 길이:"))
    size=int(input("라인두께:"))
    turtle.pencolor("red")
    turtle.pensize(size)
    
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

elif a=="사각형":
    length1=int(input("가로 길이:"))
    length2=int(input("세로 길이:"))
    size=int(input("라인두께:"))
    turtle.pencolor("blue")
    turtle.pensize(size)
    
    for i in range(2):
        turtle.forward(length1)
        turtle.right(90)
        turtle.forward(length2)
        turtle.right(90)
turtle.done()