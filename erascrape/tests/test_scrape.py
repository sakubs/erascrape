import unittest
import sys
sys.path.append('..')

from scrape import make_soup, parse_era_info


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
        # For a bad url the soup should be None
        self.assertEqual(soup, None)
        
    def test_parse_era_info(self):
        """
        Want to test that all of the era names, start dates, and end dates are 
        returned from the function.
        """
        soup = make_soup()
        era_info = parse_era_info(soup)
        print(era_info)


if __name__ == "__main__":
    unittest.main()