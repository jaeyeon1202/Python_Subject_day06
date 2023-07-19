menu={"김밥":2000,"라면":3500,"어묵":1000}

print(menu)
print(menu.keys())

# 형변환 함수
print(list(menu.keys()))
print(tuple(menu.keys()))
print(set(menu.keys()))

print(menu.values())
print(menu.items())

name={100:"황복동",200:"황채연",300:"황나연"}
print(name)

print(name[100])
#print(name[400])

print(name.get(100,"없습니다."))
print(name.get(400,"없습니다."))

#딕트 조작함수 pop()/del()
del(name[100])
print(name)

print(name.pop(200))
print(name)