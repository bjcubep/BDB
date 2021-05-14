# -*- coding:utf-8 -*-
from random import randint

# for : 컬렉션 탐색 / 반복 횟수 명확할 때
# while : 반복 조건이 명확할 때 (특정 조건을 만족하는 상황까지)

# while 조건식:
#     조건 만족하면 실행
# while True:   무한루프, 무조건 맞는 식
#     실행
#     if 조건문

# 반복문 제어 
#    break : 반복문 끝
#    continue : 강제로 다시 반복시키는 명령어, 기본 turn 종료

# 1~10 다 더하면 얼마?
sum = 0
for i in range (1, 11):
    sum += i
    print(sum)
sum2 = 0
v2 = 0
# 1+2+.....+? >= 100
while sum2 < 100:
    v2 += 1
    sum2 += v2
print(v2)
print(sum2)
print("----------")

# x에 음수 쓸 때까지
x = int(input("x : "))
y = int(input("y : "))
print(x+y)

while x >= 0:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x+y)
print("----------")

for v in range(10):
    print(v)
    if v % 2 == 1:  # v가 홀수면 멈춰라
        break
    print("ㅋ")
print("----------")

for v in range(10):
    print(v)
    if v % 2 == 1: 
        continue
    print("ㅋ")
print("----------")

a = randint(3, 6)  # 3~(6-1)까지 랜덤한 숫자를 뽑아 줌
print(a)

# 1~20사이의 랜덤한 숫자 계속 출력
# 13 나오면 끝
b = randint(1, 20)
print(b)
while b != 13:  # if문처럼 사용
    b = randint(1, 20)
    print(b)
print("----------")

# x에 음수 쓸 때까지
while True:     #무한루프, 무조건 맞는 조건
    x = int(input("x : "))
    y = int(input("y : "))
    print(x+y)
    
    if x < 0:
        break
print("----------")


randint(4, 6)