import requests
from bs4 import BeautifulSoup


def make_soup(siteurl):
    """
    Uses requests to query a webiste and attempt to parse it into a beautiful 
    soup.

    siteurl: URL for the website to parse.

    returns: the beautiful soup tree.
    """
    response = requests.get(siteurl)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup