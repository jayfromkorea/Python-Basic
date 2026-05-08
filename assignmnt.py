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

    # Getters
    @property
    def Title(self):
        return self.__title
    
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
    
    # Setters
    @Title.setter
    def Title(self, title):
        self.__title = title
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

    def display_article(self):
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
        
        


# 1. Select country
# 2. Select category
# 3. Take a look at the roaster
# 4. Choose an article
# 5. Show the info of the article

test = News()
test.Url = test.make_url()
test.display_article()
