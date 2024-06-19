import requests
from bs4 import BeautifulSoup

def get_coordinates()->list:
    nazwa_miejscowości = input('podaj nazwę miejscowości: ')

    url:str=f'https://pl.wikipedia.org/wiki/{nazwa_miejscowości}'
    response=requests.get(url)
    # print(response.text)
    response_html=BeautifulSoup(response.text,'html.parser')
    # print(response_html)
    response_html_lat: list = response_html.select('.latitude')[1].text.replace(',', '.')
    response_html_lng: list = response_html.select('.longitude')[1].text.replace(',', '.')
    print (response_html_lat)
    print (response_html_lng)
    return [response_html_lat, response_html_lng]

get_coordinates()