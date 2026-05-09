import requests as rq
from typing import Final
import os

class News:
    API_KEY:Final = 'd2fd5e1b8b50454aa36d768721b20201'
    BASE_URL:Final = 'https://newsapi.org/v2/top-headlines'


    def __init__(self):
        self.__title = ''
        self.__description = ''
        self.__category = ''
        self.__url = ''
        self.__publisher = ''
        self.__author = ''
        self.__date = ''

    # Getters
    @property
    def Title(self):
        return self.__title
    @property
    def Author(self):
        return self.__author
    @property
    def Description(self):
        return self.__description
    @property
    def Category(self):
        return self.__category
    @property
    def Url(self):
        return self.__url
    @property
    def Publisher(self):
        return self.__publisher
    @property
    def Date(self):
        return self.__date
    
    # Setters
    @Title.setter
    def Title(self, title):
        self.__title = title
    @Author.setter
    def Author(self, author):
        self.__author = author
    @Description.setter
    def Description(self, description):
        self.__description = description
    @Category.setter
    def Category(self, category):
        self.__category = category
    @Url.setter
    def Url(self, url):
        self.__url = url
    @Publisher.setter
    def Publisher(self, publisher):
        self.__publisher = publisher
    @Date.setter
    def Date(self, date):
        self.__date = date

    def choose_country(self):
        while True:
            os.system('cls')
            print('Countries available:')
            print('1. US')
            print('===============')
            print('x. exit')
            print('===============')
            choice = input('Please choose a country: ')
            if choice.lower() == 'x':
                return 'x'
            if choice >= '1' and choice <= '1':
                match choice:
                    case '1':
                        self.Category = 'The United States'
                        return 'us'
                    
    def choose_category(self):
        while True:
            os.system('cls')
            print('Categories available:')
            print('1. Business')
            print('2. Entertaiment')
            print('3. Health')
            print('4. Science')
            print('5. Sports')
            print('6. Technology')
            print('===============')
            print('x. exit')
            print('===============')
            choice = input('Please choose a category: ')
            if choice.lower() == 'x':
                return 'x'
            if choice >= '1' and choice <= '6':
                match choice:
                    case '1': return 'business'
                    case '2': return 'entertainment'
                    case '3': return 'health'
                    case '4': return 'science'
                    case '5': return 'sports'
                    case '6': return 'technology'


    def make_url(self):
        country = self.choose_country()
        if country == 'x':
            return 'x'
        category = self.choose_category()
        if category == 'x':
            return 'x'
        url = f'{self.BASE_URL}?country={country}&category={category}&apiKey={self.API_KEY}'
        return url

    def choose_article(self):
        if self.__url == 'x':
            print('Exiting...')
            exit(-1)
        res = rq.get(self.__url)
        if res.status_code != 200:
            print('Cannot retreive data from the website')
            exit(-1)
        
        result = res.json()

        if result['status'] != 'ok':
            print('Invalid articles')
            exit(-1)

        print(f'The number of articles: {result['totalResults']}')
        for each_art in range(0, len(result['articles'])): # each_art: an index of a list of each article containing info such as title, author, source,etc.
            feature = result['articles'][each_art]
            print(f'Article #{each_art + 1}')
            print(f'Title: {feature["title"]}')
            print(f'Author: {feature["author"]}')
            print(f'Description: {feature["description"]}')
            print(f'URL: {feature["url"]}')
            print(f'Date: {feature["publishedAt"]}')
            print(f'Publisher: {feature["source"]["name"]}')
            print() # Line change

        while True:
            choice = int(input('Please choose the number of the article you like: '))
            if choice >= 1 and choice <= len(result['articles']):
                break
        choice -= 1 # 0-based indexing

        self.Title = result['articles'][choice]['title']
        self.Author = result['articles'][choice]['author']
        self.Description = result['articles'][choice]['description']
        self.Publisher = result['articles'][choice]['source']['name']
        self.Url = result['articles'][choice]['url']
        self.Date = result['articles'][choice]['publishedAt']

    def __repr__(self) -> str:
        return f'Title: {self.Title}\n Author: {self.Author}\n Date: {self.Date}\n Category: {self.Category}\n Description: {self.Description}\n URL: {self.Url}\n Publisher: {self.Publisher}\n======================='
        # print(f'Title: {self.Title}')
        # print(f'Author: {self.Author}')
        # print(f'Date: {self.Date}')
        # print(f'Category: {self.Category}')
        # print(f'Description: {self.Description}')
        # print(f'URL: {self.Url}')        
        # print(f'Publisher: {self.Publisher}')


        


# 1. Select country✅
# 2. Select category✅
# 3. Take a look at the roaster✅
# 4. Choose an article
# 5. Show the info of the article

test = News()
test.Url = test.make_url()
test.choose_article()
print(test)

business5 = News()
business5.Url = business5.make_url()
business5.choose_article()
print(business5)