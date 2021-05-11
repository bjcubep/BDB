# -*- coding:utf-8 -*-

# list, numpy : 인덱스로 접근

# set(집합) : 중복을 알아서 제거, 순서? random  
s = {10, 20, 30, 20, 40, 10}
print(s, type(s))
# print(s[0]) 인덱싱 안됨 --> list로 바꿔서 사용
s = list(s)
print(s, type(s))
print(s[0])

# list가 주력
l = [1, 2, 3, 4, 5, 6, 7, 6, 3, 5]
# list의 중복을 없애고 싶을 때 set에 넣었다 빼면 없어진다
l = set(l)      # set으로 변환
l = list(l)     # 다시 list로 변환
print(l)
print("-----------")

# dict : 순서 개념x, 키:값(key:value) 형태
d = {"사과":500, "감자":300}
print(d["사과"])

# key값이 없으면 추가, 있으면 수정, 중복된 key값은 들어갈 수 없음
d["배추"] = 1000
d["사과"] = 300
print(d) 

k = list(d.keys())          # 키만 추출해서 활용 가능
print(k)
v = list(d.values())        # 값만 추출
print(v)

# 일반적으로 데이터를 list와 dict의 형태로 표현

