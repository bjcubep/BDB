# -*- coding:utf-8 -*-
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[123, 4, 34, 1], [54, 12, 3, 4]])
c = np.array([10, 20, 30, 40])

# 항목별로 계산 수행, 또 다른 np array로 반환
q = a + b       
print(q)
# broadcasting 차원 높은 쪽에 맞춰서 항목별 계산, np array로 반환
w = a + c       
print((w))
print("------------")

# indexing : 데이터에 접근
print(a[0])         
print(a[0, 1])
print(a[0, 1:3])
print(a[:, 0])  # : 전체에서, index 0만 [1, 5]

a[0, 1:3] = 100  # indexing해서 한번에 바꾸기
a[:, 0] = 500
print(a)

name = np.array(["홍", "김", "이"])
age = np.array([10, 20, 30])
height = np.array([180, 170, 160])
weight = np.array([100, 60, 90])
parent = np.array([["홍판서", "홍어머니"], ["김판서", "김엄니"], ["이아빠", "이엄마"]])

# masking : 조건으로 조회
#     조건식을 수행해서 만족하는 인덱스들이 결과값으로 나오는 구조
print(age[age >= 20])
print(age[(age >= 5) & (age <= 25)])    # and/or --> &/| 사용
print(age[name == "홍"])     #이름이 "홍"인 사람의 나이

print(name[age >= 20])  # 나이가 20살이상인 사람 이름들
print(name[(age >= 5) & (age <= 20)])
print("----------------")

# 다이어트해야하는 사람 이름
# 표준체중 = (키 - 100) * 0.9
# 비만도 = (몸무게 / 표준체중) * 100 
# 비만도 120 넘으면 비만
standardWeight = (height - 100) * 0.9
bimando = (weight / standardWeight) * 100
print(name[bimando > 120])
print(standardWeight)
print(bimando)

print(parent[bimando >120])     # 다이어트해야하는 사람 부모님
print(parent[bimando >120, 0])      # 다이어트해야하는 사람 아버지이름









