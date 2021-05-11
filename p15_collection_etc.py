# -*- coding:utf-8 -*-

# Python에만 있는 collection

# range (numpy의 arange와 같은 기능) : 범위 표현
r = range(10)
print(r, type(r))
# 0 ~ 9까지 차례대로 들어있는 list가 필요할 때 형변환하여 사용 
l = list(r)
print(l) 

rr = range(10)  # 숫자 하나만 쓰면 0 ~ (10-1)
ll = list(rr)
print(ll)

rr = range(3, 10)  # 숫자 하나만 쓰면 3 ~ (10-1)
ll = list(rr)
print(ll)

rr = range(3, 10, 2)  # 숫자 하나만 쓰면 0 ~ (10-1)까지 2칸씩(step)
ll = list(rr)
print(ll)
print("--------------")

# tuple : list와 거의 동일한 기능, collection의 용도 보다는 다른 식으로 활용
t = (10, 20, 30, 10, 50)  
print(t, type(t))
print(t[0])  # indexing 가능

# a, b 값 바뀌게
a = 10
b = 20
print(a, b)
# c = a        다른 언어의 경우 변수 하나가 더 필요
# a = b
# b = c
# print(a, b)

# 변수 2개 값을 바꿀 때 tuple 사용
(a, b) = (b, a)  # python에만 있는 기능
print(a, b)
# x = 1
# y = 2
# z = 3
(x, y, z) = (1, 2, 3)   # 변수 여러 개 만들어서 한 번에 값 넣은 것 가능
(x, y, z) = (z, x, y)
print(x, y, z)
(q, w, e, r) = (6, 7, 8, 9)   # q, w, e = 9, 6, 4  괄호 생략 가능 / 소스를 대폭 줄여 줌 ^^
print(q, w, e, r)

height, weight = float(input("키 : ")), float(input("몸무게 : "))  # 한 줄로 처리 가능 but 가독성 고려하여 적정 수준으로...
print(height, weight)








