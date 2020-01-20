import requests

from bs4 import BeautifulSoup
from dbhandler import create_connection, create_table


def run():
    response = requests.get('http://houshinji.org/calendar.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    eras = soup.find_all(class_='era')
    for era in eras:
        
        for child in era.parent.parent.children:
            try:
                print(child.text)
            except AttributeError:
                print(child)

    conn = create_connection()
    create_table(conn)
    
    