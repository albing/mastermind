import unittest

import engine

class test_engine(unittest.TestCase):
    def test_right_guess(self):
        self.assertEqual(engine.check_guess([1,2,3,4], [1,2,3,4]), (4,0))

    def test_wrong_order(self):
        self.assertEqual(engine.check_guess([1,2,3,4], [4,3,2,1]), (0,4))

    def test_duplicates_in_answer(self):
        self.assertEqual(engine.check_guess([1,1,2,2], [1,2,3,4]), (1,1))

    def test_duplicates_in_guess(self):
        self.assertEqual(engine.check_guess([1,2,3,4], [1,1,2,2]), (1,1))

    def test_duplicates_in_guess_and_answer(self):
        self.assertEqual(engine.check_guess([5,6,6,5], [5,5,6,6]), (2,2))

if __name__ == '__main__':
    unittest.main()
