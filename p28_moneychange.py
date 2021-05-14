# -*- coding:utf-8 -*-

# 물건 가격 :
# 낸 돈 :
# 거스름 돈 ?

# 잔돈 리스트로 만들어서 나눈 몫이 그 단위 돈 갯수, 빼고 남은 것 또 나눈 몫
# 오만원짜리 = 거스름돈 // 50000
# 거스름돈 // 10000
# 거스름돈 // 5000

cost = int(input("물건 가격 : "))
payment = int(input("낸 돈 : "))
change = payment - cost
print(change)

cMoney = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# for i in range(len(cMoney)):
    # z = cMoney[i]
    # if change >= z:
        # x = change // z         # 몫 = 갯수
        # change -= (z * x)       # 나눈 단위 금액 빼주기
        # print(z, x)             # 단위, 객수 출력

t = 0    
for v in cMoney:
    t = change // v
    print("%d원짜리 : %d개" %(v, t))
    change %= v
print("----------")

cost = int(input("물건 가격 : "))
payment = int(input("낸 돈 : "))
change = payment - cost
print(change)

money = 50000
r = 0
while True:
    r = change // money
    print("%d원짜리 : %d" %(money, r))
    change %= money
    money /= 5
    
    r = change // money
    print("%d원짜리 : %d" %(money, r))
    change %= money
    money /= 2
    
    if money == 5:
        break
