from freezegun import freeze_time
from datetime import datetime
import unittest


class MyTests(unittest.TestCase):

    @freeze_time("1955-11-12")
    def test_the_class(self):
        assert datetime.now() == datetime(1955, 11, 12)

    def test_custom(self):
        assert datetime.now() != datetime(1955, 11, 12)

    def test_custom2(self):
        with freeze_time('2012-01-01'):
            assert datetime.now() == datetime(2012, 1, 1)
        assert datetime.now() != datetime(2012, 1, 1)
            
if __name__ == '__main__':
    unittest.main()

