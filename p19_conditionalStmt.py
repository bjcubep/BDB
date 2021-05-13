# -*- coding:utf-8 -*-

# 조건문 : 조건 따져서 실행  ★ 중요  
# if 조건식:
#    실행문     (들여쓰기로 영역 구분)  
# else:
#    그거 아니면

# if 조건식A:
# elif 조건식B:
#     조건식 A->X, 
#     조건식 B 만족 시 실행문
# else:
#     (그거 아니면)실행문

age = int(input("나이 : "))
print(age)

# 나이가 19살 미만 : 나가 출력 
# 19 <= 나이 : 어서오세요 
# 60 < 나이 <= 70 : 어유 어서오십쇼 
# 70초과 : 안녕하십니까
#
if age < 19:       # 다른 언어는 if(조건식) 괄호 있어야하지만 파이썬은 괄호 생략 가능
    print("나가")
elif age <= 60:
    print("어서오세요")
elif age < 70:
    print("어유 어서오십쇼") 
else:
    print("안녕하십니까")
print("-------------")

# 조건문, 반복문, 컬렉션, 자유로움에서 나오는 혼돈 제어, 분석용 데이터 구축

# 나이가 20살 이상이면 : 어서오세요 출력
# 나이가 짝수면 : ㅋ 출력
# 나이가 4의 배수면 : ㅎ 출력
if age >= 20:
    print("어서오세요")
if age % 2 == 0:
    print("ㅋ")
if age % 4 == 0:
    print("ㅎ")
print("-------------")

# 국,영,수 점수를 넣어서 
# 평균이 80점 넘으면 잘했다 출력
# 60 <=평균 <80 노력해라
# 60점 미만 재시험
# 함수를 만들어서

def say(s):
    avg = (s[0]+s[1]+s[2]) / 3
    print(avg)
    if avg >= 80:
        print("잘했다")
    elif 60 <= avg:
        print("노력해라")
    else:
        print("재시험")
        
score = [20, 90, 70]  #파라메터로 리스트가 주어짐
say(score)      # 함수 호출
say([30, 50, 40])
say([100, 80, 90])

# 숫자 2개를 넣었을 때 더 큰 숫자를 찾아주는 함수
def getBigger(x, y):
    if x > y:
        return x        # x값을 return하고 끝, else 필요 없이 if 라인에서 return y하면 된다
  # else:             
      # return y
    return y 
    
z = getBigger(3,5)
print(z)




