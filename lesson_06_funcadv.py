# 가변길이 매개변수를 받아서 해당 아이템들을 리스트로 묶어서 반환
def to_list(*items:int):
    li = []
    for i in items:
        li.append(i)    
    return li

def to_list2(*items:int):
    li = list(items)    
    return li

def to_list3(*items:int):
    return [i*i for i in items]

def to_list4(*items:int):
    return [ i*i for i in items if i%2 == 0 ]

def to_dict(tp1, tp2):
    '''두개의 시퀀스를 받아서 하나의 딕셔너리로 만들기'''
    di = {}
    for k, v in zip(tp1, tp2):  # zip()은 함수가 아닌 class임
        di[k] = v
    return di

def to_dict2(tp1, tp2):
    '''두개의 시퀀스를 받아서 하나의 딕셔너리로 만들기'''
    di = {k: v for k, v in zip(tp1, tp2)}
    return di


l = to_list(1,2,3,4,5,6)
print(l)

l2 = to_list2(1,2,3,4,5,6)
print(l2)

l3 = to_list3(1,2,3,4,5,6)
print(l3)

l4 = to_list4(1,2,3,4,5,6)
print(l4)

print(to_dict((1,2,3,), ('하나','둘','셋',)))
print(to_dict('한둘셋', '123'))
print(to_dict2((1,2,3,), ('하나','둘','셋',)))