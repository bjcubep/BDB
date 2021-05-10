# -*- coding utf-8 -*-
from time import sleep

# 콘솔창에 출력, 줄바꿈 print 
print("박경화")

# 출력 줄 안바꾸고 한줄에
print("출력을", end=" ")
print('줄 안바꿔서 한줄에', end=" ")
print('나온다')

print("큰따옴표 \" 는 역슬래시를 하고")
print('"')
#특수문자 
# \" : "  
# \' : '
# \n : 줄바꿈 (newline)
# \r : 커서 맨 앞으로 (carriage return)      
# /r/n 커서 맨앞으로 가서 줄바꿈, 완벽한 줄바꿈 but 파이썬은 해당 안 됨 \n만 써도 줄바꿈 완성 
# \t : tab 다음 포인트로 가기
# \b : back-space 한 글자(1byte) 지우기
# \\ : 역슬래시
# 경로 표시할 때 사용  D:\\Kwon\\bus2020.csv"
# %% : %를 글자로 쓸 때는 두 번 쓴다 

print("\"")
print('\'')
print("ㅁㅁㅁ\nㅍㅍㅍ")
print("ㅁㅁㅁ\rㅍㅍㅍ")
print("ㅁㅁㅁ\r\nㅍㅍㅍ")

print("이 름\t: 박")
print("주 소\t: 수원")

print("ㅋㅋㅋ\b")
print("aaa\b")

print("\\")

print("D:\\Kwon\\bus2020.csv")

# 형식지정
'''
문자열 : %s
정수 : %d   %03d : 3자리  %02d " 2자리  %05d : 5자리
실수 : $f   %.3f : 소수점이하 3자리 반올림
'''
#정수
print("%d" % 8)
print("%05d" % 8)
print("i%02d.png" % 3)

#실수
print("%f" % 3.142578)
print("%.3f" % 3.142578)
print("%.4f" % 3.142578)
print("%.1fcm" % 169.452)

#문자열

print("이름 : %s" % "박경화")
print("키 : %.1fcm, 몸무게 : %.2fkg" %(180.123, 70.3453))

print("%.1f%%" % 80.123)    #80.1% 출력, %를 글자로 쓰려면 두번 적어준다


print("*************************\n* 이름\t: %s\t*\n* 주소\t: %s\t\t*\n* 나이\t: %d세\t\t*\n* 키\t: %.1fcm\t*\n*************************" %("박경화", "수원", 48, 169.32))

sleep(5)















