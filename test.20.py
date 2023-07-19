# # 1000%3==0 3의배수
# # 1000%5==0 5의배수

# a=[]
# a.append
# if  1000% 3 ==0:
s=0
for num in range(1000):
    if num % 3 ==0 or num%5==0:
        #print(num)
        s += num
print(s)