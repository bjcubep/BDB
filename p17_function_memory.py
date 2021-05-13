# -*- coding:utf-8 -*-

d = 10
e = 10
def test(a, b, c):
    print("test-------")
    print(a)
    print(b)
    print(c)
    # print(d)
    a = 100
    b[0] = 100
    c = [100, 200]
    # d = 100        함수 속에서 변수 작업 : 새로 만드는 d로 인식, 9행에서 에러 발생
    global e        # 밖에 있는 그 e
    e = 100 
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print("test-------")

####################################
a = 10
b = [10, 20]
c = [10, 20]
test(a, b, c)
print(a)
print(b)
print(c)
print(d) 
print(e)
