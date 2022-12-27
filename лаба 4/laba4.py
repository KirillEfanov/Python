import pandas as pd
from pandas import read_csv
import requests
from functools import reduce
from bs4 import BeautifulSoup

def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list

