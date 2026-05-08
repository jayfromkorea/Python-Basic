
class Person:
    country = 'Korea'   # 클래스 멤버 변수

    # 생성자(Constructor): 클래스를 이용하여 인스턴스를 생성하는 아주 특별하 매서드
    def __init__(self, name, age):
        self.__age = age    #__age
        self.name = name  #__name 이와 같이 __를 사용하면 외부에서 바꾸지 말라는 뜻임 컨벤션임
        # 왜냐하면 파이썬에는 public, private, protected가 없기 때문임

    # class method
    @classmethod
    def change_country(cls, country:str):
        cls.country = country


    @property
    def Age(self):  # getter: 외부에 값을 노출하는 기능
        return self.__age   
    
    @Age.setter
    def Age(self, age):
        if age < 0:
            return
        self.__age = age

        # representation
    def __repr__(self):
        return f'{self.name}({self.__age})'
    
    def __eq__(self, value):
        if not isinstance(value, Person):
            return False
        
        return self.name == value.name and self.__age == value.__age

    # 클래스 안의 함수들은 Method라고 부름
    def introduce(self):    # 인스턴스 메서드(Insatnace Method)
        print(f'안녕하세요, 제 이름은 {self.name}이고 나이는 {self.__age}살입니다')



# 클래스 상속(Inheritance)
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age) # 부모 클래스의 생성자를 호출해줌
        self.grade = 'First Grade'
        self.total = 0
        self.avg = 0.0

    # 매서드 재정의(Method Override)
    def introduce(self):
        super().introduce()
        print(f'{self.grade}학년입니다.')

    
    
    
        
            
    #def __str__(self):  # 위의 함수와 같은 함수
    #    return f'{self.name}({self.age})'
    
    def exam(self, kor, eng, math):
        self.total = kor + eng + math
        self.avg = self.total / 3

    def print_exam(self):
        print(f'총점: {self.total}, 평균: {self.avg}')

class MyUnit:
    def __init__(self):
        self.hp = 100
        self.attack = 50
        self.speed = 200

#object: 모든 클래스의 조상 클래스(최상위 클래스)

# Person클래스를 이용하여 hong intance를 생성하다.
hong = Person('홍박사', 20)
#num = int(15)
#name = str('홍길동')
#hong.age = 20
#hong.name = '홍박사'
hong.introduce()
#print(hong.name, hong.age)

iu = Person('아이유', 30)
iu.introduce()

iu2 = Person('아이유', 30)


lee = Person('이순신', 100)
lee.introduce()

kim = Student('김민식', 44)
kim.exam(50, 60, 70)
kim.print_exam()
kim.introduce()
print(kim) #    __repr__

num = 10
score = 10

if num == score:
    print('같음')

if iu == iu2:   # iu __eq__(iu2)와 같음
    print('The same')
else:
    print('Different')


print(isinstance(num, int))
print(isinstance(num, str))
print(isinstance(num, object))

print(isinstance(hong, Person))
print(isinstance(hong, object))
print(isinstance(hong, Student))
print(isinstance(kim, Student))
print(isinstance(kim, Person))
print(kim)

hong.__age = 30 # 에러는 발생하지 않음
hong.introduce()
hong.Age = 30   # property
hong.introduce()

Person.country = '대한민국'
hong.country = 'Korea'
iu.country = '미국'
bang = Person('방우식', 67)
print(hong.country)
print(bang.country)

Person.change_country('Some Country')
print(Person.country)
hong.change_country('Taiwan')   # cls는 Person으로 자동 대입
print(hong.country)