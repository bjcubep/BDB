# -*- coding:utf-8 -*-
# 데이터 - 저장
#    CPU(연산장치) :
#    RAM(저장장치) : 변수(variable)형태로 임시저장
#        RAM전체 - 재부팅하면 자동삭제
#        stack / static - 프로그램 종료 시 자동 삭제
#        heap - 사람이 직접 삭제해야 함
#            Python : Garbage Collection 
#                    heap 자동 삭제 - 언제? 데이터 있는 번지를 가리키는 변수가 없으면
#                                프로그램이 종료되면서 stack이 자동 삭제되면서 heap도 정리가 됨
#    HDD/SSD(저장장치) : 파일형태로 영구저장
#        파일을 따로 지워야 데이터가 삭제 됨
#    GPU(그래픽처리용(CPU+RAM+HDD)) :
########################################################################################
# '=' 우항에 있는 것을 좌항에 넣으라는 의미 (같다X, 같다는'==') 
# 왜가 아니고 언제 사용하는지에 집중
# 변수(variable) : 데이터를 임시로 저장, 데이터를 담는 그릇
#    변수명 = 데이터
#    변수명 : 마음대로 설정, 의미를 알기 쉽게 의미가 나타나도록
#            숫자로 시작X, 특수문자X, 파이썬문법X

a = 10 # a라는 변수 만들어서 10 저장
print(a) # a에 저장되어 있는 데이터 출력
print(id(a))
a = 45621.2315  # a에 저장된 값 바꾸기 python만 가능
print(a) 
print(id(a))
# b라는 변수 만들어서 123.423저장, ㅠdp에 저장되어 있는 데이터 출력
b = 123.423
print(b)
print(id(b)) # id 주소값 stack에 있는 값 출력
b = None # 이 변수가 어떤 번지도 가리키지 않게 -> Garbage Collection발동(heap 삭제)

# 정수 : 4bytes
# 실수 : 8bytes
#       static 변수  |  stack 번지값 64bit  |  heap 번지값과 실데이터
#      다른 언어는 stack에 바로 번지값과 실데이터를 저장 
# 파이썬은 똑같은 데이터를 표현하는데 메모리를 많이 사용,  사람이 활용하기는 편리함
print("------")

# 기본 데이터 자료형 : int, float, str, bool
test = 10 #정수
print(test) # 변수에 저장되어 있는 값
print(id(test)) # 데이터가 있는 메모리 주소
print(type(test)) # 자료형, python은 자료형을 알아서 처리해 줌

test=123.345 #실수
print(type(test))

test = "글자"  #텍스트
print(type(test))

test = True #boolean
print(type(test))
print("------")

# 형변환 : 자료형(데이터)
x = 123
x = str(x)
print(type(x))
x = float(x)
print(type(x))













