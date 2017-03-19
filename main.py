from freezegun import freeze_time
from datetime import datetime
import unittest


# class TestDates(unittest.TestCase):
#     def testDate(self):
#         with freeze_time("2012-01-01"):
#             assert datetime.datetime(2012, 1, 1) == datetime.now()


@freeze_time("1955-11-12")
class MyTests(unittest.TestCase):
    def test_the_class(self):
        assert datetime.now() == datetime(1955, 11, 12)

        
if __name__ == '__main__':
    unittest.main()
