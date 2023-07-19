# 세트 자료형: 중복없음, 순서없음

a={1,2,3,4,3,3,3}
print(a)

A={10,20,30}
B={20,40}


print(A&B)  #교집합
print(A.intersection(B))

print(A|B)   #합집합
print(A.union(B))

print(A-B)   #차집합
print(A.difference(B))