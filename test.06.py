count={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

print(count[0])
print(count[1])

for x in range(1,1001):
    for i in str(x):  #x값을 문자열로 변환
        count[int(i)]=count[int(i)]+1
print(count)