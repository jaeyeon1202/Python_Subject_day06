a=10,20,30,40
print(a)
print(a[0])
print(a[-1])
print(a[1:])
print(a[:2])
print(type(a))

tt1=(10,20,30,40)
tt2=("A","B")
print(tt1)
print(tt2)
print(tt1+tt2)
print(tt2*3)

# 이차원 튜플
tt=((1,2,3),(4,5,6),(7,8,9))
print(tt)
print(tt[0])
print(tt[0][0])
print(tt[1])
print(tt[2])

for i in range(3):
    for j in range(3):
        print(tt[i][j],end="")
    print("")


