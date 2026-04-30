import requests as rq
from typing import Final
import os

API_KEY:Final = 'd2fd5e1b8b50454aa36d768721b20201'

'''
카테고리를 선택 입력받아서 해당 카테고리에 대한 뉴스 기사들을 가져오는 프로그램을 구현하시오
'''

os.system('cls')    # 화면 클리어

def get_menu() -> str:
    os.system('cls')    # 화면 클리어
    print('1. Business')
    print('2. Entertaiment')
    print('3. Health')
    print('4. Science')
    print('5. Sports')
    print('6. Technology')
    print('===============')
    choice = int(input('Please choose a category: '))
    while choice < 0 or choice > 6:
        print('Please choose between 1 and 6')
        choice = int(input('Please choose a category: '))
    match choice:
        case 1: return 'Business'
        case 2: return 'Entertaiment'
        case 3: return 'Health'
        case 4: return 'Science'
        case 5: return 'Sports'
        case 6: return 'Technology'

def menu():
    while True:
        os.system('cls')    # 화면 클리어
        print('1. Business')
        print('2. Entertaiment')
        print('3. Health')
        print('4. Science')
        print('5. Sports')
        print('6. Technology')
        print('===============')
        choice = int(input('Please choose a category: '))
        if choice >= 0 and choice <= 6:
            match choice:
                case 1: return 'Business'
                case 2: return 'Entertaiment'
                case 3: return 'Health'
                case 4: return 'Science'
                case 5: return 'Sports'
                case 6: return 'Technology'

user_choice = menu()
print(user_choice)


res = rq.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=d2fd5e1b8b50454aa36d768721b20201')
if res.status_code != 200:
    print('요청한 사이트로부터 데이터를 바을 수 없음')
    exit(-1)    #프로그램 종료

#print(type(res.json()))
result = res.json()

if result['status'] != 'ok':
    print('Invalid Request, Cannot Retrieve data')
    exit(-1)

print(f'전체뉴스 기사 개수: {result["totalResults"]}')

articles = result["articles"]   # 타입은 list이다
print(type(articles))
for article in articles:
    print(f"제목: {article['title']}")
    # description
    # url
    # author
    # publishedAt
    # source.name
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}")
    print(f"Author: {article['author']}")
    print(f"Date: {article['publishedAt']}")
    print(f"Publisher: {article['source']['name']}")
    print()