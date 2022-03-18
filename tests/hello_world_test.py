import hello_world    # The code to test
import unittest   # The test framework

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(hello_world.add(2, 3), 5)

    def test_zero_add(self):
        self.assertEqual(hello_world.add(2, 0), 2)

if __name__ == '__main__':
    unittest.main()
