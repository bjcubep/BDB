# -*- coding:utf-8 -*-

# 문자열, 리스트 모두 인덱스로 슬라이싱 가능
s = "가나다라 마바사아 자차카타  파하ㅎㅎ ㅋㅋㅋㅋ ㅎㅎㅎㅎ"
print(s)
print(s[3])
print(s[2:8])
print(s[:15])
print(s[-6])

# 변수명 = """ """, ''' ''' 큰따옴표 또는 작은따옴표 3세트 사이에 작성한 내용이 그대로 출력
ss= """ㅎㅎㅎㅎㅎ
ㄴㄴㄴㄴㄴ
ㅇㅇㄷㅎㅈㄴㅇ
ㄴㅇㅀ"""
print(ss)

# 변수1 = 데이터1
# 컬렉션 (python 기본제공(list, set, tuple, dictionary), numpy, pandas, ...)  
# 변수1 = 데이터n
# list 
kor = [100, 90, 80, 70, 50]
print(type(kor))
print(kor) # 전체
print(kor[1]) # 변수명[인덱스] : 인덱스는 0부터, (특정데이터에 인덱스로 접근 0,1,2,3,4)
print(kor[2:4]) # 범위접근(슬라이싱) 인덱스 2번부터 4번 전까지 2 ~ (4-1)
print(kor[:4]) # 처음부터 숫자-1까지 0 ~ (4-1)
print(kor[1:]) # 1 ~ 끝까지 1,2,3,4
print(kor[0:4:2]) # [시작:끝:간격] 0~3까지 2칸씩 띄고
print(kor[-1]) # 뒤에서 부터, 뒤에서 첫 번째 (마이너스는 1부터)
print("----------------")

name = ["가가가", "나나나", "다다다"]
print(name)                    # 전체
print(name[0])                 # 0번 데이터
print(name[-2])                # 뒤에서 두번째 데이터
print(name.index("다다다"))    # 다다다는 몇번에 Index값 반환
print("그그그" in name)        # 그런 데이터가 있는지 확인 True/False


name.append("마마마")          # 맨 뒤에 데이터 추가
name.insert(1, "사사사")       # 특정 위치에 추가
name[3] = "라라라"             # 수정
name.remove("마마마" )         # 데이터 삭제 (데이터로)
del name[1]                    # 데이터 삭제 (위치, 인덱스로)

name.sort()                     # 오름차순 정렬
name.sort(reverse=True)         # 내림차순 정렬

print(len(name))               # 데이터 수
print(name)

print("-------------")
eng = [30, 70, 100, 80, 90, 85, 45, 60, 20, 55, 95, 88, 77, 66, 98]
print(len(eng))     # 몇 명
eng.sort(reverse=True)
print(eng[0]) # 1등 몇점
print(eng[-1]) # 꼴등 몇점
print(eng[len(eng)-1]) 

# print(max(eng))     # 1등 몇점
# print(min(eng))     # 꼴등 몇점
# print(sum(eng))















