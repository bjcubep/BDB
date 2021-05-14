# -*- coding:utf-8 -*-
from random import randint

# for i in range(6):
    # lotto = randint(1, 46)
    # print(lotto, end=" ")
    #
# print(sLotto)    

l = []  # 빈 리스트 하나 만들고

while True :
    l.append(randint(1, 45))        # 1~45에서 랜덤하게 숫자 뽑아서 list에 추가
    l = set(l)      # list를 set으로 형변환 {} 중복 제거
    l = list(l)     # 다시 쓸 수 있게 list로 형변환 []
    if len(l) == 6:    # l은 리스트 
        break
print(l)


