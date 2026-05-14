# open: 파일의 데이터를 저장하거나, 파일로부터 데이터를 읽기 위해 파일 핸들을 얻는다
# open('C:\\Users\\User\\Downloads\\test.txt')이것도 되고 밑에것도 됨
'''
r: read mode로 열기, 파일이 무조건 있어야 함, 없으면 실패함
w: write mode로 열기, 무조건 새 파일로 만듦, 파일이 없어도 open에 성공함
a: append mode로 열기, 파일이 있으면 해당 파일을 열고, 없으면 w모드와 동일하게 동작함

t: text mode, 텍스트 데이터를 다루기 위해 open
b: binary mode, 

'w+'
'''

import csv, json


def read_text_file_all(filename:str):
    try:
        # with: System Resource(file, memory, network ...)를 자동으로 반납할 수 있도록 처리해주는 명령문(블럭)
        with open(filename, 'rt', encoding='utf-8') as f:   #여기서 open()은 with구문이 작동할 때만 작동하고, 끝나면 자동으로 close
            txt = f.read()
            if txt == '': 
                print()
                return
            print(txt)                
    except FileNotFoundError as e:
        print(f'{filename}파일을 찾을 수 없습니다.')

def write_text_file(filename:str, txt:str):
    with open(filename, 'wt', encoding='utf-8') as f:
        f.write(txt)



def read_text_file_chunk(filename:str, chunk_size=8):
    try:
        # with: System Resource(file, memory, network ...)를 자동으로 반납할 수 있도록 처리해주는 명령문(블럭)
        with open(filename, 'rt', encoding='utf-8') as f:   #여기서 open()은 with구문이 작동할 때만 작동하고, 끝나면 자동으로 close
            
            while True: #
                # chunk_size만큼만 f로부터 읽어들여 txt에 저장
                txt = f.read(chunk_size)
                if txt == '': 
                    print()
                    return
                print(txt, end='')                
    except FileNotFoundError as e:
        print(f'{filename}파일을 찾을 수 없습니다.')

def read_text_file_line(filename:str):
    try:
        # with: System Resource(file, memory, network ...)를 자동으로 반납할 수 있도록 처리해주는 명령문(블럭)
        with open(filename, 'rt', encoding='utf-8') as f:   #여기서 open()은 with구문이 작동할 때만 작동하고, 끝나면 자동으로 close
            
            while True: #
                txt = f.readline()  # 줄 단위로 읽음
                if txt == '': 
                    print()
                    return
                print(txt, end='')                
    except FileNotFoundError as e:
        print(f'{filename}파일을 찾을 수 없습니다.')

def read_text_file_lines(filename:str):
    li = []
    try:
        # with: System Resource(file, memory, network ...)를 자동으로 반납할 수 있도록 처리해주는 명령문(블럭)
        with open(filename, 'rt', encoding='utf-8') as f:   #여기서 open()은 with구문이 작동할 때만 작동하고, 끝나면 자동으로 close
            li = f.readlines()  # 줄 단위로 읽어서 list에 저장
            print(txt, end='')                
    except FileNotFoundError as e:
        print(f'{filename}파일을 찾을 수 없습니다.')

    return li

def write_csv_file(filename:str, li:list):
    with open(filename, 'wt', encoding='utf-8', newline='') as f:
        # f(파일)에 접근 가능한 csv writer 객체를 생성
        writer = csv.writer(f)
        # writer.writerow() # 반복문을 이용하여 li의 모든 내용을 저장
        writer.writerows(li)

def read_csv_file(filename:str):
    with open(filename, 'rt', encoding='utf-8') as f:
        # 여기서 reader는 반복 가능한 객체
        reader = csv.reader(f)
        for row in reader:
            print(row)

def write_json_file(filename:str, data:dict):
    with open(filename, 'w', encoding='utf-8') as f:
        # data(dictioanry)를 f(파일)에 덤프(저장)
        # dumps는 dictionary를 string형태로 바꿈
        json.dump(data, f)

def write_json_file2(filename:str, data:dict):
    with open(filename, 'wt', encoding='utf-8') as f:
        # 데이터의 양이 많지 않을 경우 문자열로 변환가능
        json_text = json.dumps(data)
        print(json_text)
        f.write(json_text)  # 문자열로 변환된 데이터를 파일에 저장

        
def read_json_file(filename:str):
    with open(filename, 'rt', encoding='utf-8') as f:
        di = json.load(f)
        print(di)


if __name__ == '__main__':
    read_text_file_all(r'C:\Users\User\Downloads\test.txt')

    txt = 'File Successfully Written, 성공적으로 처리'
    write_text_file('write_test.txt', txt)
    read_text_file_chunk(r'C:\Users\User\Downloads\test.txt')    
    read_text_file_line(r'C:\Users\User\Downloads\test.txt')
    print(read_text_file_lines(r'C:\Users\User\Downloads\test.txt'))
    li = [
        ['번호', '이름', '학과', ],
        ['01', '김철수', '경영학과'],
        ['02', '김민지', '교육학과'],
        ['03', '김구라', '영어영문학과'],
        ['04', '이수지', '독어독문학과']
    ]

    write_csv_file('test.csv', li)
    read_csv_file('test.csv')

    di = {
        'count' : 4,
        'data' : [
            {'번호' : 1, '이름' : '김철수', '학과' :  '경영학과'},
            {'번호' : 2, '이름' : '김민지', '학과' :  '한문학과'},
            {'번호' : 3, '이름' : '이수철', '학과' :  '영어영문학과'},
            {'번호' : 4, '이름' : '안철수', '학과' :  '독어독문학과'},
        ]
    }

    write_json_file('test.json', di)
    read_json_file('test.json')