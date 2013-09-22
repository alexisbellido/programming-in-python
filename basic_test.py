import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        """
        Make sure shuffled sequence does not lose elements.

        """
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertNotEqual(1, 2)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
