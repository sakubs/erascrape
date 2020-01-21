from erascrape.scrape import make_soup


def test_make_soup():
    url = 'http://houshinji.org/calendar.html'
    
    soup = BeautifulSoup(response.content, 'html.parser')
    