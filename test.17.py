a=["국어","영어","수학"]
b=[]
s=0

for i in range(len(a)):
    score=int(input(a[i]+"점수:"))
    b.append(score)
    s += b[i]
avg=s/3
print("총점:",s)
print("평균: %.2f" % avg)

if avg>=80:
    print("잘함")
elif 70<=avg<=79:
    print("보통")
else:
    print("미흡")