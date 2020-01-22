import requests
from bs4 import BeautifulSoup


def make_soup(siteurl = 'http://houshinji.org/calendar.html'):
    """
    Uses requests to query a webiste and attempt to parse it into a beautiful 
    soup.

    siteurl: URL for the website to parse. Initialized to the site this library 
    is written to parse data from. To use a different url is not supported, 
    but you may modify this code to handle other sites if you like in your own 
    programs.

    returns: the beautiful soup tree.
    """
    try:
        response = requests.get(siteurl)
    except requests.exceptions.ConnectionError:
        print("Passed a bad url")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def parse_era_info(soup):
    """
    Given a soup structure, it will parse the soup and pull the relevant 
    information.

    Prerequisites: make_soup has successfully returned a soup that is not 
    None
    """
    pass