'''
두개의 저수와 1개의 연산자(문자열)을 입력바아서 연산을 수행하고 결과를 반환하는 함수를 저의하고 호출하세요
함수이름: calculate
Parameters: num1, num2, op

op: +, -, *, /, %

return 해당 결과값
'''
print(__name__)
def calculate(num1:int, num2:int, op:str):
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '%':
            return num1 % num2
        
if __name__ == '__main__':
    print(calculate(10, 15, '+'))
    print(calculate(10, 15, '-'))
    print(calculate(10, 15, '*'))
    print(calculate(10, 15, '/'))
    print(calculate(10, 15, '%'))
    print('Succesfully executed')
    print()

def calculate2(*nums:int):
    MAX = nums[0]
    MIN = nums[0]
    sum = 0
    for i in nums:
        if i > MAX:
            MAX = i
        elif i < MIN:
            MIN = i
        sum += i
    avg = sum / len(nums)

    return sum, avg, MAX, MIN

print(calculate2(1,3,5,7,9))

def make_vow(msg:str):
    ret = ''
    for i in msg:
        match i:
            case 'a': ret += i
            case 'e': ret += i
            case 'i': ret += i
            case 'o': ret += i
            case 'u': ret += i
    
    return ret

def make_vow2(msg:str):
    vowels = 'aeiou'
    ret = ''
    tmp = msg.lower()
    for i in tmp:
        if i in vowels: ret += i
    
    return ret

print(make_vow('appleaeioubgfds'))

def my_counter(*nums:int):
    ret = {}
    for i in nums:
        if i not in ret:            
            ret[i] = 1
            #print(f'{i} not in the dict! --> {ret[i]}')
        else:
            #print(f'currently: {ret[i]}')
            ret[i] += 1
            #print(f'{i} in the dict! --> {ret[i]}')

    return ret

print(my_counter(1,2,2,2,3,3,3,3,3,4,4,5,5,5,5))