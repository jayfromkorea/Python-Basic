import json, os
import requests as rq

class NewsRequester:
    categories = {
        1 : ['general', '일반'],
        2 : ['business', '경제'],
        3 : ['entertainment', '예능'],
        4 : ['sports', '스포츠'],
        5 : ['health', '건강'],
        6 : ['technology', '첨단기술'],
        7 : ['science', '기초과학']
    }
    def __init__(self, config_file:str):
        '''read_configuration()을 호출하여 환경설정'''
        self.__api_key = ''
        self.__base_url = ''
        self.__country = ''
        self.articles = []
        self.read_configuration(config_file)
        

    def read_configuration(self, config_file):
        '''config_file로부터 설정값 읽어서 인스턴스 변수에 설정'''
        with open(config_file, 'r', encoding='utf-8') as f:
            di = json.load(f)
            self.__api_key = di["API_KEY"]
            self.__base_url = di["BASE_URL"]
            self.__country = di["COUNTRY"]
        

    def show_configuration(self):
        '''설정된 환경 변수값을 출력함'''
        '''출력형식
        API_KEY = ................
        BASE_URL = https//...........
        COUNTRY = us
        '''
        print(f'API_KEY = {self.__api_key}')
        print(f'API_KEY = {self.__base_url}')
        print(f'API_KEY = {self.__country}')

    @classmethod
    def select_menu(cls):
        while True:
            os.system('cls')
            # class 변수 categories로부터 key, value의 형식으로 가져옴
            for k, item in cls.categories.items():
                print(f'{k}: {item[0]}, {item[1]}')

            print('------------------')
            selected = input('번호를 입력하세요: ')
            if selected in '1234567':
                return cls.categories[int(selected)][0]
            
    def get_articles(self, category:str) -> int:
        ...
        url = f'{self.__base_url}?country={self.__country}&category={category}&apiKey={self.__api_key}'
        req = rq.get(url)
        req.raise_for_status.get()  # 200(ok)가 아니면 Exception 발생함
        result = req.json()
        if result['totalResults'] == 0:
            raise rq.HTTPError('가져올 뉴스 데이터가 없습니다.')
        self.articles = result["articles"]
        return len(self.articles)
        #return result["articles"]
    
    # articles라는 맴버 변수에 result["articles"] 저장
    # 반환은 가져온 기사 개수


if __name__ == '__main__':
    news_req = NewsRequester('new_config.json')
    news_req.show_configuration()
    category = NewsRequester.select_menu()
    # print(category)
    print(f'Total number of articles retreived: {news_req.get_articles(category)}')
    # 가져온 기사의개수: 
    