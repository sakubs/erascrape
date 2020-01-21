import unittest
import sys
sys.path.append('..')

from scrape import make_soup


class TestScrape(unittest.TestCase):
    """
    Test suite for testing functions in the scrape module.
    """

    def test_make_soup_good_url(self):
        """
        Want to make sure that the url can be parsed properly, and also that it 
        handles errors gracefully.

        Give it a good url.
        """
        url = 'http://houshinji.org/calendar.html'
        soup = make_soup(url)
    
    def test_make_soup_bad_url(self):
        """
        Want to make sure that the url can be parsed properly, and also that it 
        handles errors gracefully.

        Give it a bad url.
        """
        # bad url
        url = 'http://housinji.org/calendar.html'
        soup = make_soup(url)

    


if __name__ == "__main__":
    unittest.main()