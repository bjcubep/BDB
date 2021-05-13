# -*- coding:utf-8 -*-

# 반복문
#    컬렉션을 탐색
# for 변수명 in 컬렉션명:
#    내용
l = [11, 12, 13, 14, 15, 16]
for v in l:  # 반복하면서 v에 차례대로 l값 대입
    print(v)
print("---------")
# 숫자 0 ~ 5까지 출력
l = [0, 1, 2, 3, 4, 5]
for i in l:
    print(i)
print("---------")
# 3 ~ 7까지 출력
# for(int i = 3; i <8; i++) 다른언어에는 있는 이 기능이 파이썬에는 없음
l = list(range(3, 8))  # 방법1. range를 list로 바꿔서 사용 가능 
for i in l:
    print(i)
print("---------")
for i in range(3, 8):  # 방법1 간소화해서 파이썬 반복문 문법 
    print(i)
print("---------")

# ㅋ를 5번 출력
for i in range(5): 
    print("ㅋ")
print("---------")

# 반복문 속에서 변수 만드는거 자제 (컴터 폭발?...)
q = 0   #변수 생성
for v in range(3):
    q = v               # 값만 바꿈 (변수q를 for문 밖에서 만들어서 v를 담는다) 
    w = v               # 변수 생성, 값바꿈 (for문 안에 새로운 변수가 계속 만들어진다 (stack과 heap에) 메모리 낭비) 
    print(q, w)
print("---------")

# 1 + 2 + 3 + ... + 10 = ?
a = 0
for i in range(1, 11):
    a += i      # a += i 는 a = a + i 와 같다   
print(a)
print("---------")

# 10!  = 1*2*3*...*10
f = 1
for i in range(1, 11):
    f *= i
print(f)
print("---------")

# 1 ~ 20 1,3,5,7,...19까지
for i in range(1, 21, 2):   
    print(i)
print("---------")

# 10, 8, 6, ... 0
for i in range(10, -1, -2):
    print(i)
print("---------")

#1, ㅋ, 3, ㅋ...19
for i in range(1, 20):   
    if i % 2 != 0:
        print(i)
    else:
        print("ㅋ")
print("---------")

# 1 ~ 20 홀수는 더하고, 짝수는 빼면?
h = 0
for i in range(1, 21):
    if i % 2 != 0:
        h += i
    else:
        h -= i
print(h) 




#    단순 반복

