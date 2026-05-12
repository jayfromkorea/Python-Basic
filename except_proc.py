# 에러의 종류
# 1. Syntax Error: 발생시 컴파일러가 빨간줄을 그어줌, easy to spot
# 2. Runtime Error: 발생되면 안됨, 파이썬에서 Exception이라고 부름
# 3. Logical Error: 발생되면 안됨


# 예외 처리
# ZeroDivision, ValueError(형변환시), TypeEror('10' + 5 등), IndexError, KeyError(딕셔너리에서 없는 키를 access할때), AttributeError(class에 없는 매서드나 변수 사용시)
# 만약에 아래의 코드가 함수였다면, 그리고 num1 / num2을 반환한다면, finally를 사용해 어떠한 값을 반환해야할 때 활용가능
try:
    #fh = open('파일')   # 시스템 리소스를 획득

    num1 = int(input('첫번째 정수 입력하세요: '))
    num2 = int(input('두번째 정수 입력하세요: '))
    try:
        num1 / num2
    except Exception:
        print(e)

    print(num1 / num2)
    
except (ZeroDivisionError, ValueError) as e:
    print(e)
except IndexError as e:
    print(e)
    #print('Invalid Value')
except RuntimeError as e:
    print(e)
except Exception as e:
    print(e)
else:   # Exception이 발생되지 않았을 때 실행됨 (거의 사용되지 않음)
    print('No error occured')
finally:
    print('This is executed no matter what happens')
    #fh.close()  # 시스템 리소스 반납

tot = 0
li = [1,2,3,4,'5',6]

count = len(li)
proc = 0
skip = 0


for n in li:
    try:
        tot += n
        proc += 1
    except TypeError as e:
        # tmp = int(tot)  # 이렇게 살리려고 할 필요가 없음, 또 다른 에러를 불러올 수 있음
        # 검증된, 안정된 코드를 넣을 것
        skip += 1
        continue

print(f'total: {tot}, elements: {count}, skipped elements: {skip}')


print('Successfully Terminated')