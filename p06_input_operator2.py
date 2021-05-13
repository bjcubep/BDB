# -*- coding:utf-8 -*-
# 데이터의 특징을 고려해서 자료형을 설정해 줌
# name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))
print("--------------------------")
# print("내이름은 %s입니다. 키는 %.1fcm이고, 나이는 %d살입니다" % (name, height, age))
print("키는 %.1fcm이고, 나이는 %d살입니다" % (height, age))

# 논리연산자(>, <, >=, <=, ==, !=) 결과로 True / False

a = (height >= 150)      # 키가 150이상인지
print(a)

b = (age < 20)      # 나이가 20살 미만
print(b)

c = (height == 170)         # 키가 170인지
print(c)

d = (age != 30)         # 나이가 30살이 아닌지
print(d)

e = (age % 2 == 0)       # 나이가 짝수인지
print(e)
# 논리결합연산자( and(&), or(|), not)
# and, or : 더 이상 검사할 필요 없으면 중간에 끝나는 버전
# &, | : 더 이상 검사할 필요 없어도 끝까지 가는 버전
# and = &&, or = ||, xor = ^
f = (height >= 150) and (age < 20)       # 키가 150이상이고, 나이가 20살 미만인지 &
g = (height >= 150) or (age < 20)        # 키가 150이상이거나, 나이가 20살 미만인지 |
print(f, g)
h = not g       #g결과의 반대
print(h)

# 놀이공원 
# and 둘 다 맞아야 True, or 둘 중 하나만 맞아도 True
# and 확률 낮은 조건식 앞에 배치, or 확률 높은 조건식 앞에 배치  => 컴퓨터의 연산 횟수가 줄어 듦
# (and는 앞에 확률이 낮은 것을 적어주어 걸러주고, or은 앞에 확률이 높은 것을 적어준다)
# i = (age >= 5) and (height >= 200) #나이가 5살 이상이고, 키가 200cm 이상인 
i = (height >= 200) and (age >= 5)  # 앞에 걸러줄 수 있는 조건을 적어서 작업 효율을 높여준다. 앞이 맞아야 뒤에 작업하기 때문

# j = (height >= 200) or (age >= 5)    # 키가 200cm 이상이거나, 나이가 5살 이상인
j = (age >= 5) or (height >= 200)    # 참인 가능성이 많을 조건을 앞에 적어 준다. 뒤에 조건 작업 안하게
print(i, j)

# eXlusive OR (xor : 배타적OR) : 조건식 2개가 다르면 O  (^)
# OO -> X, OX -> O, XO -> O, XX -> X
k = (age >= 5) ^ (height >= 200)   #키가 200이상이든지, 나이가 5살 이상이든지 하나만
print(k)

l = (age >= 5) and (age <= 10)  # 5살부터 10살까지







