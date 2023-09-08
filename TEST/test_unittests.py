import unittest   # The test framework

# custom function 
def foo(a,b):
    return a+b

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)
    # test unit of custom function foo
    def test_foo(self):
        self.assertEqual(foo(3,4),7)

if __name__ == '__main__':
    unittest.main()