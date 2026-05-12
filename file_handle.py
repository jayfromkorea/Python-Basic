# open: 파일의 데이터를 저장하거나, 파일로부터 데이터를 읽기 위해 파일 핸들을 얻는다
# open('C:\\Users\\User\\Downloads\\test.txt')이것도 되고 밑에것도 됨
'''
r: read mode로 열기, 파일이 무조건 있어야 함
w: write mode로 열기, 무조건 새 파일로 만듦, 파일이 없어도 open에 성공함
a: append mode로 열기, 파일이 있으면 해당 파일을 열고, 없으면 w모드와 동일하게 동작함

t: text mode, 텍스트 데이터를 다루기 위해 open
b: binary mode, 

'w+'
'''
f = open(r'C:\Users\User\Downloads\test.txt', 'rt', encoding='utf-8')
txt = f.read()
print(txt)
f.close()