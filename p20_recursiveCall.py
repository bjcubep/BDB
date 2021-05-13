# -*- coding:utf-8 -*-

# 함수 : 정리 차원에서는 좋음, 함수 호출하면 속도 느려짐 

# factorial
# 1! = 1
# 2! = 2*1       = 2*1!
# 3! = 3*2*1     = 3*2!
# 4! = 4*3*2*1   = 4*3!
# 5! = 5*4*3*2*1 = 5*4!

# 숫자 하나를 넣었을 때 팩토리얼 구하는 함수 3! = 1 * 2 * 3
def getFactorial(n):
    if n == 1:
        return 1
    return n * getFactorial(n-1)
# return 4 * getFactorial(3)
#    return 3 * getFactorial(2)
#        return 2 * getFactorial(1)
b = getFactorial(10)
print(b)

# 피보나치 수열 (첫번째1, 두번째1, 세번째부터는 앞에 두자리 수의 합)
# 1 1 2 3 5 8 13 21 34 55...
# getFibo(1) = 1
# getFibo(2) = 1
# getFibo(3) = getFibo(2) + getFibo(1)
# getFibo(4) = getFibo(3) + getFibo(2)
# ... 5, 8, 13, 21, 34, 55, 89 ...

# 숫자 하나 넣으면 그 위치의 피보나치 수열 값 구해주는 함수
def getFibo(n):
    if n <= 2:       # n이 1이거나 2이면 1, 3부터는 앞에 두자리를 더한 값
        return 1
    return getFibo(n-1) + getFibo(n-2)

c = getFibo(6)
print(c)

print("----------")

# 함수를 recursive(재귀적)으로 호출 : 함수 속에서 자기 자신을 또 호출, 반복이 생김

# 내가 원하는 결과가 나와야 하는데 안나올 때 원하는 결과가 나올 때까지 반복할 때
# 예를 들어 회원가입 시 id나 pw 입력, 국적입력 등등

def getNationality():
    where = input("국적(한국 or 기타) : ")
    if where == "한국" or where == "기타":
        return where
    return getNationality()     # 원하는 값을 입력하지 않으면 다시 돌아가서 입력

w = getNationality()
print(w)






