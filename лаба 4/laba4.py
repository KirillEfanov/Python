import pandas as pd
from pandas import read_csv
import requests
from functools import reduce
from bs4 import BeautifulSoup

def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list

#созданный список
old_list = ['1', '2', '3', '4', '5']
new_list = list(map(old_list, int))
for i in range(len(new_list)):
    new_list[i] = new_list[i] + 5
print(new_list)

#датасет
df = pd.read_csv('country.csv', sep=',')
df1 = df[(df.people > 500000)]
print("Количество стран c населением больше 500000:  ", reduce(lambda a, x: a + 1, df1, 1))

#парсинг
arr_quotes = []
url = 'https://www.kinoafisha.info/rating/movies/2022/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='rating_num')
for i in quotes:
    arr_quotes.append(i.text)
print("Количество фильмов с оценкой 7.0: ", reduce(lambda a, x: a + x.count('7.0'), arr_quotes, 0))
