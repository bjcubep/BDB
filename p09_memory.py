# -*- coding:utf-8 -*-

a = 10
aa = [10, 20]
aaa = [10, 20]
print(a, id(a))
print(aa, aa[0], id(aa))
print(aa, aaa[0], id(aaa))
print("---------")

b = a               # a변수에 들어있던 stack 번지 값(id) b에 넣어 줌 heap값은 새로 생기지 않음 
bb = aa             # bb변수에 aa변수의 stack 번지 값 넣어 줌 heap값 생성 X
bbb = aaa           # bbb변수에 aaa변수의 값 넣어줌 (stack 번지 값, heap 새로 생성x)
print(b)
print(bb, bb[0])
print(bbb, bbb[0])
print("---------")

c = 100             # stack에 새 번지 생성, heap에 데이터 생성 
bb[0] = 100         # stack 번지 그대로, heap값 (aa = bb) 첫인덱스가 100으로 변경
bbb = [100, 200]    # stack 새 번지 생성, heap값 새로 생성
print(c)
print(bb, bb[0])
print(bbb, bbb[0])
print("---------")

print(a) 
print(aa, aa[0]) 
print(aaa, aaa[0])



