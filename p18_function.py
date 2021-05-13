# -*- coding:utf-8 -*-
from time import sleep

# 1) 함수 정의  
#    parameter : 함수를 수행하는데 필요한 데이터
#                호출하는 쪽 -> 함수내부로 보내는 데이터
#    return : 함수 수행 결과
#             함수내부 --> 호출하는 쪽으로 보내는 데이터

# def 함수명(변수명, 변수명, 변수명, ...):
#    내용


# 숫자 2개 넣으면 그 합을 출력하는 함수
def printHab(a, b):
    print(a + b)

    
printHab(10, 20)


# 숫자 2개를 넣으면 그 합을 구하는 함수
def getHab(a, b):
    hab = a + b
    return hab  # 변수 hab을 함수를 호출한 쪽으로 보내주기, 함수 끝
    print("aaa")  # return값 다음에 적은 명령어는 수행 안함 왜? 함수가 이미 끝났으니까


x = getHab(20, 30)
print(x)


# 리스트에서 제일 큰 값 구하는 함수
def getBiggest(l):
    l.sort(reverse=True)
    maxNo = l[0]  # maxNo는 함수 안에서만 사용 가능한 변수
    return maxNo  # return을 통해서 함수 밖에서 호출 가능
    # print("제일 큰 값은 : "+str(l[0]))
    # l.sort()
    # print(l[-1])

 
# 숫자를 넣으면 사칙연산결과를 구하는 함수
def getCalc(a, b):
    h = a + b
    c = a - b
    g = a * b
    m = a / b
    # gc = (h, c, g, m)     # tuple로 결과를 담아서 return    
    # return gc  # return은 여러개 적용 불가
    return h, c, g, m  # 괄호가 생략된 tuple이다. 여러개를 적은 것이 아니다.     
#            4개 리턴된 것 처럼 보이지만 tuple 하나 리턴


#######################################################################
z = getCalc(30, 20)
print(z)
print("------------")

a, s, d, f = getCalc(30, 40)  # a,s,d,f로 받은 것처럼 보이지만 tuple의 문법 특성을 활용한 것
print(a)
print(s)
print(d)
print(f)
print("-------------")

# 함수 중 일부만 사용하고 싶을 때 _
w, t, _, _ = getCalc(10, 20)     
print(w)
print(t)
print("-------------")

# 2) 함수 호출
# 함수명(값, 값, 값, ...)

a = [2, 3, 4, 1, 5]
c = getBiggest(a)
# print(a)
# (a에서 제일 큰 수) 동안 기다렸다
sleep(c)
b = [4, 2, 6, 3, 8]
q = getBiggest(b)
print(q)

# lambda 함수 : 이름(함수명) 없는, 1회용 함수
# lambda 변수명, 변수명, ... : 내용

# 숫자를 2개 넣으면 그 합 출력하는 함수
(lambda a, b : print(a + b))(100,200)

# 숫자 2개 넣으면 그 합 구하는 함수
k = (lambda a, b : a + b)(3,5)     # lambda 함수식을 변수에 담아 출력하면 됨
print(k)

