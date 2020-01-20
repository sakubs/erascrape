import requests
from bs4 import BeautifulSoup

def run():
    response = requests.get('http://houshinji.org/calendar.html')
    soup = BeautifulSoup(response.content, 'html.parser')

    eras = soup.find_all(class_='era')
    for era in eras:
        print(era)