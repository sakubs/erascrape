import requests

from bs4 import BeautifulSoup
from dbhandler import create_connection, create_table, insert_era


def run():
    """
    Main entry point for the app.
    """
    response = requests.get('http://houshinji.org/calendar.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    eras = soup.find_all(class_='era')
    cleaned_eras = []
    
    counter = 0
    # Need to strip out whitespace and get only the tags with relevant text.
    era_id = 1
    for era in eras:
        cleaned_era = [era_id]
        for child in era.parent.parent.children:
            try:
                cleaned_era.append(child.text.strip())
            except AttributeError:
                continue
        cleaned_eras.append(cleaned_era)
        era_id += 1

    conn = create_connection()
    with conn:
        create_table(conn)

        for era in cleaned_eras:
            insert_era(conn, era)