# -*- coding:utf-8 -*-

# 조건문
# 반복문
# 컬렉션

# dict값을 가진 list
products = [
            {"이름":"키보드", "가격":10000},
            {"이름":"마우스", "가격":35000},
            {"이름":"쿨링패드", "가격":23000},
            {"이름":"이어폰", "가격":17000},
            {"이름":"케이블", "가격":9000},
            {"이름":"마우스패드", "가격":8000},
          ]
# 상품 몇 종류
print("상품종류 :", len(products))
# 첫 번째 상품명
print("첫번째 상품명 :", products[0]["이름"])    
# 마지막 상품 가격
print("마지막 상품 가격 :", products[-1]["가격"])
print("----------")

# 평균가
avg = 0
sum = 0

for v in products:
    sum += v["가격"]    
print("총합 :", sum)
avg = sum / len(products)
print("평균가 :", avg)

# 최고가
maxPrice = 0
for v in products:
    if maxPrice < v["가격"]:
        maxPrice = v["가격"]
print("최고가 :", maxPrice)
print("----------")

# 제일 비싼 상품명
for v in products:
    if maxPrice == v["가격"]:
        print("제일 비싼 상품 :", v["이름"], maxPrice)
print("----------")

# 평균가보다 비싼 상품명들
for v in products:
    if avg < v["가격"]:
        print("평균가보다 비싼 상품들 :", v["이름"], v["가격"])
        
# products : 상품들이 있는 list
# products[0] : list의 첫번째 데이터 (상품dict)
# products[0]["가격"] : list의 첫번째 데이터의 가격(가격 int)

print(type(products[0]["가격"]))

