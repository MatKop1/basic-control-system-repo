import unittest
from .. import app
 
class TestSum(unittest.TestCase):
 
    def test_area(self):
        sq = app.Square(2)
 
        self.assertEqual(sq.area(), 4,
            f'Area is shown {sq.area()} rather than 9')
 
if __name__ == '__main__':
    unittest.main()