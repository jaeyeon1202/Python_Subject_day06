import random
a=[]
for i in range(10):
    a.append(random.randint(0,9))
print(a)

for i in range(10):
    if i not in a:
        print(i, end="")
print("")