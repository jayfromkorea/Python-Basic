from typing import Final

AGE_ERROR_MSG:Final = '나이는 음수가 도리 수 없습니다'

# Exception 정의
class AgeError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)

class AgeError1(RuntimeError):
    def __init__(self, *args):
        super().__init__(f'{AGE_ERROR_MSG} ({args[0]})')

# li에는 음수가 들어있으면 안됨
def avg_age(li):
    try:
        tot = 0
        for age in li:
            # 예외(Exception)를 유발시켜서 logic error 찾기
            if age < 0:
                raise AgeError1(age)
            tot += age
        return tot / len(li)
    except ZeroDivisionError as e:
        print('리스트에 데이터가 없습니다')
        return 0

try:
    li = [30, 25 , 28, 43, 7, -18, 39]
    avg_age(li)
except RuntimeError as e:
    print(e)

# 리스트에서 value를 찾아 해당 value의 인덱스를 반환하는 함수
def find_value(li:list, value): # 이와 같이 Exception을 직접 설계할 경우 아래처럼 독스트링을 써주는게 좋음
    '''
    주어진 list에서 value를 찾아 해당 인덱스 반환,<br>
    찾지 못 한 경우에는 ValueError가 발생됨
    '''
    # return li.index(value)
    for i, v in enumerate(li):
        if v == value:
            return i
        
    raise ValueError(f'리스트에서 값 {value}을 찾을 수 없습니다')

find_value()