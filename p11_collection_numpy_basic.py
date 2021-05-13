# -*- coding:utf-8 -*-

# kor = [100, 90, 80]
# eng = [60, 70, 50]
# examSum = kor + eng
# print(examSum)
# kor[0:2] = 0

# Python, Java : 전 세계적으로 많이 사용하는 major한 언어 
#                -> 자료가 많음
#                -> library 사용하기 편하게 시스템이
# library : 다른 누군가가 기능을 만들어서 공개
# framework : library + tool
# 인공신경망 (tensorflow)

# Python의 library 관리시스템 : pip 
#        cmd -->  pip install 이름

# NumPy : list에 분석용으로 이런저런 기능 추가 
#        pip install numpy

import numpy as np      # numpy 불러와서 앞으로는 np라는 이름으로 사용

test = np.array([[10, 20],[30, 40],[50, 60]])        #array 생성
print(test)             # 전체
print(test[0])          # 특정데이터 접근
print(test[0][1])       # 기존 list 스타일
print(test[0, 1])       # numpy 스타일

print(test.shape)       # 몇 행 몇 열인지
print("----------")

test = np.zeros([3,2])          # 0으로 shape채워서 생성
print(test)
print(test.shape)
print("----------")

test = np.ones([3,2])          # 1로 shape채워서 생성
print(test)
print(test.shape)
print("----------")

test = np.arange(10)          # 0~(10-1)까지 값 채워서 생성
print(test)
print(test.shape)
print("----------")

test = np.arange(5, 10)          # 5~(10-1)까지 값 채워서 생성
print(test)
print(test.shape)
print("----------")

kor = np.array([100, 90, 80])       #NumPy array생성(python list)
eng = np.array([60, 70, 50])
print(kor)          # 전체
print(kor.shape)            # 모양
print(kor.dtype)            # 데이터 자료형

kor[0:2] = 0                # slicing(범위 지정해서 값 처리)
print(kor)
examSum = kor + eng         # 항목별 합계 
examAvg = (kor + eng) / 2
print(examSum)
print(examAvg)

