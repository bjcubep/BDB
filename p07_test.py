# -*- coding:utf-8 -*-
# 변수명은 소문자로 시작
# 띄어쓰기 대신 _ (뱀체), 중간 대문자(낙타체)

# 키:  몸무게:   
#  1. 표준체중 출력 = (키 - 100) * 0.9  / 2. 비만도 출력 = (몸무게 / 표준체중) * 100 
# 3. 위험 : 비만도가 120% 이상, 몸무게가 200이상

height = float(input("키: "))
weight = float(input("몸무게 : "))
print("-----------")
s_weight = (height - 100) * 0.9
o_weight = (weight / s_weight) * 100
print("표준체중\t: %.1fkg" % s_weight)
print("비만도\t\t: %.1f%%" % o_weight)
danger = (o_weight >= 120) or (weight >= 200)
print(danger)

# 비만도가 130넘고, 비만도가 150넘는거
