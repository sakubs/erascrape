import unittest
import sys
sys.path.append('..')

from dbhandler import create_connection, create_table, ERASCRAPE_DB, insert_era
from scrape import make_soup, parse_era_info


class TestDbHandler(unittest.TestCase):
    """
    Test suite for testing functions in the dbhandler module.
    """

    def test_make_connection(self):
        """
        Need to test the function can make db connections reliably.
        """
        create_connection("test.db")
        
    def test_create_table(self):
        conn = create_connection("test.db")
        create_table(conn)

    def test_insert_era(self):
        soup = make_soup()
        eras = parse_era_info(soup)
        conn = create_connection("test.db")
        create_table(conn)
        #Test multiple entries.
        record_id = 1
        for era in eras:
            era.append(record_id)
            insert_era(conn, era)
            record_id += 1

        #Test a double input attempt.
        insert_era(conn, eras[0])

        #Test a bad input
        insert_era(conn, [1, '2', '3'])


if __name__ == "__main__":
    unittest.main()