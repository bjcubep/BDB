# -*- coding:utf-8 -*-

# ctrl(왼쪽) + f11 : run  실행
# f11 : bebug
#    f6 : 다음 줄로 이동

l = ["ㅁ", "ㄴ", "ㄹ"]

for v in l:     # 반복문이 진행되면서 l의 값 하나 하나가 v에 저장
    print(v)
     
for i, v in enumerate(l):       # index도 같이 사용하고 싶을 때 i-index, v-value
    print(i, v)
print("----------")    

l = [1, 2, 3]
l2 = [10, 20, 30]

for v in l:
    for v2 in l2:
        print(v, v2)
print("----------")

# 구구단 2단
for v in range(1, 10):
    print("2 * %d = %d" %(v, 2*v))
print("----------")

# 구구단 전체
for dan in range(2, 10):        #단 고정 2,3,4....9
    print("%d 단 -----" % dan)
    for num in range(1, 10):        # 숫자변화 1,2,3....9
        print("%d * %d = %d" %(dan, num, dan*num))

# 2*1=2 3*1=3 4*1=4...9*1=9 가 먼저 한줄 출력되고 다음으로 넘어가는 형태(단변화*숫자고정)
# 첫자리가 변하고 뒷자리가 고정인 형태
# end="\t"로 구구단 사이 간격 조절,  print() 한줄 입력하고 다음줄로 넘어가는 엔터 역할
for i in range(1, 10):
    for j in range(2, 10): 
        print("%d * %d = %d" %(j, i, j*i), end="\t")
    print()

for v in range(1, 10):      # 숫자 변화
    for dan in range(2, 10):    # 단 고정      
        print("%d * %d = %d" %(dan, v, dan*v), end="\t")
    print()
print("----------")

# 별찍기 
#1
for i in range(5):
    for j in range(i+1):
        print("ㅋ", end="")
    print()
print("----------")
#2
for i in range(5):
    for j in range(5-i):
        print("ㅋ", end="")
    print()
print("----------")

#3 
for i in range(5):
    for j in range(5):
        if i == j:
            print("ㅋ", end="")
        else:
            print("  ", end="")
    print()
print("----------")

for i in range(5):
    for j in range(i+1): 
        if i == j:
            print("ㅋ", end="")
        else:
            print("  ", end="")
    print()

for i in range(5):
    for j in range(i):     # i=0 j=-1 ㅋ / i=1 j=0 공백 ㅋ (j는 공백, j만큼 띄고 i출력) 
        print("  ", end="")
    print("ㅋ", end="")
    print()
print("----------")    

#4  (j가 홀수면 ㅋ, 짝수면 ㅎ)
for i in range(5):
    for j in range(i+1):
        if j % 2 == 0:
            print("ㅋ", end="")
        else:
            print("ㅎ", end="")
    print()
print("----------")

#5 
for i in range(5):
    for j in range((i*2)+1):
        if i % 2 == 0:
            print("ㅋ", end="")
        else:
            print("ㅎ", end="")
    print()

# i값이 홀수인지의 판별은 i반복문 아래에서 진행하는 것이 효율적
# 변수하나를 만들어서 조건이 변하는 경우의 실행문을 저장
# j반복문에서 출력
t = None            
for i in range(5):
    if i % 2 == 0:
        t = "ㅋ"
    else:
        t = "ㅎ"
    for j in range((i*2)+1):
        print(t, end="")
    print()



    


