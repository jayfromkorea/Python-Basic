#import mod as md
from mod import my_counter as mc, calculate
#from mod2 import calculate as smth

name = '홍길동' # 전역변수 Global Variable
num = 100   # 보통 전역변수는 const(상수)로 활용하고 싶을 때 사용

def my_func(name:str):
    print(name)     # Local Variables
    global num  # 이렇게 해야 전역변수를 수정할 수 있음
    num = 10
    print(num)
    
def modify_list(li3):
    li3.append(100)

if __name__ == '__main__':  # 이렇게 쓰면 entry point로 사용
    print(__name__) # __main__
    my_func('아이유')
    print(num)
    li3 = []
    modify_list(li3)
    print(li3)


print(mc(1,2,2,2,3,3,3,3,3,4,4,5,5,5,5))
print(calculate(1, 2, '+'))