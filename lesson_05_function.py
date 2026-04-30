'''
함수(function): 정의(Define), 호출(Call) --> 반드시 정의가 먼저되어야 호출될 수 있음


def 함수이름(매개변수(들)):
    함수에서 처리할 명령문1
    함수에서 처리할 명령문2
    함수에서 처리할 명령문3
    ...
    함수에서 처리할 명령문n
    
    [return 반환값] (필요시)
'''

def add(num1:int|float, num2:int|float) -> int|float:
    '''
    add함수의 정의
    '''
    num3 = num1 + num2
    return num3

def show_hello(msg:str|None='User'):
    '''반환값이 없는 함수 정의 가능'''
    print(f'Hi, {msg}')

res = add(1, 2)     # 위치 가반 호출
print(res)
print(add(1, 2))
print(add('one', 'two'))

res = add(num2 = 2, num1 = 1)   # 이름기반 호춯
print(res)

# add('one', 2) 이건 에러가 발생함

# 이러한 함수는 소비형 함수임
res = show_hello('민수')    # None 값이 들어감
show_hello()
show_hello(5)


def total_avg(scores:list):
    '''리스트를 전달받아서 아이템들의 합계와 평균을 반환하는 함수'''
    tot = 0
    for i in scores:
        tot += i
    avg:float = tot / len(scores)
    return tot, avg    # 반환값이 여러개일시 ***튜플***로 반환함!!!


def greet(msg1, msg2='반가반가'):  # 매개변수가 여러개일 때 가장 오른쪽부터 default value를 무조건 부여해야함
    print(f'{msg1}, {msg2}')
    
    
def greet2(msg1, msg2='반가반가', msg3='ㅂㄱㅂㄱ'):  # 매개변수가 여러개일 때 가장 오른쪽부터 default value를 무조건 부여해야함
    print(f'{msg1}, {msg2}, {msg3}')
    


greet('하이요')
greet2('하이요', '바이요')
greet2('하이요', msg3='바이요')


total, avg = total_avg([1,2,3,4,5,6])
print(f'total: {total}, avarage: {avg}')

total, _ = total_avg([1,2,3,4,5,6])

li = [1,2,3,4,5]
for _ in li:
    pass
    

def my_func(name, age):
    pass    # 함수의 내용이 아직 구현되어 있지 않음
    ...     # 이것도 같은 기능임
    
print(1,2,3,4,5, sep = ' and ')

def total_avg2(*scores:int|float):  # 가변길이 매개변수 활용
    tot = 0
    for i in scores:
        tot += i
    return tot

def total_avg3(*scores:int|float, rnd:int):  # 가변길이 매개변수와 다른 변수가 있을 때는 무조건 이름지정으로 호출해야함
    tot = 0
    for i in scores:
        tot += i
    avg = tot / len(scores)
    return tot, round(avg, rnd)

def dynamic_arg(**kwargs):
    #for k, v in kwargs.items():
    #   print(f'{k}: {v}')
    print(kwargs['line'])

dynamic_arg(a='김민수', b='김철수', c=[10, 20])
dynamic_arg(num1 = 10, num2 = 90)

print(total_avg3(1,2,3,4,5, rnd=3))

print(total_avg2(1,2,3,4,5))


one = total_avg([1,2,3,4,5,6])
print(one)



