a={"구재연":"010-4586-2667","최재연":"010-7161-2667","염기주":"010-2306-0512"}

print(list(a.keys()))

name=input("찾는친구이름:")
print(a.get(name,"없습니다"))