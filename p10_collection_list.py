# -*- coding:utf-8 -*-

# list : 인덱스로 데이터에 접근

# 1차원
name = ["박", "김", "이"]
print(name[0], type(name[0]))  # 변수명[인덱스] 형태로 데이터에 접근

# 2차원 (객체를 활용하는 것이 더 효율적임)
score = [[100, 90, 70], [90, 80, 80], [80, 70, 90]]  # list속에 list 3명학생 국영수 점수
print(score[0], type(score[0]))  # 첫번째학생  국영수 전체
print(score[0][1], type(score[0][1]))  # 첫번째학생 리스트 중 1번 인덱스 영어
# 두번째 학생 수학점수
print(score[1][2])
# 첫번째 학생 평균점수
# aSum = sum(score[0])
# print(aSum)
# aAvg = aSum / len(score[0])
# print(round(aAvg))

avg = (score[0][0] + score[0][1] + score[0][2]) / 3
print(avg)

# 학생 평균 점수 출력하기
sNo = int(input("번호 입력 : ")) -1
avg = (score[sNo][0] + score[sNo][1] + score[sNo][2]) / 3
print(avg)






