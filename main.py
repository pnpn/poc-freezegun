from freezegun import freeze_time
from datetime import datetime
import unittest


@freeze_time("1955-11-12")
class MyTests(unittest.TestCase):
    def test_the_class(self):
        assert datetime.now() == datetime(1955, 11, 12)

        
if __name__ == '__main__':
    unittest.main()
