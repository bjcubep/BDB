# -*- coding:utf-8 -*-

# 중간고사 :
# 기말고사 :
# 수, 우, 미, 양, 가

# def scoreGrade():  (vicky)
    # m = int(input("중간고사 : "))
    # e = int(input("기말고사 : "))
    # avg = (m + e) / 2
    # print(m, e, avg)
    # if avg >= 90:
        # print("수")
    # elif avg >= 80:
        # print("우")
    # elif avg >= 70:
        # print("미")
    # elif avg >= 60:
        # print("양")
    # else:
        # print("가")

#scoreGrade()

# 중간고사 점수 입력
def getMidExam():
    mid = int(input("중간고사 : "))
    if 0 <= mid <= 100:
        return mid
    return getMidExam()

# 기말고사 점수 입력
def getFinalExam():
    fin = int(input("기말고사: "))
    if 0 <= fin <= 100:
        return fin
    return getFinalExam()

# 등급 (vicky)
def getGrade(a, b):
    avg = (a + b) / 2
    if avg >= 90:
        print("수")
    elif avg >= 80:
        print("우")
    elif avg >= 70:
        print("미")
    elif avg >= 60:
        print("양")
    else:
        print("가")
    
##################################

mid = getMidExam()
# print(mid)
fin = getFinalExam()
# print(fin)
print("------")
# grade = getGrade(mid, fin) 

# 수업
avg = (mid + fin) / 2

if avg >= 90:
    print("수")
elif avg >= 80:
    print("우")
elif avg >= 70:
    print("미")
elif avg >= 60:
    print("양")
else:
    print("가")

