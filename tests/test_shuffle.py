import unittest

from pycasso import shuffle, unshuffle

TEST_SEED = "Pycasso"
TEST_SEQUENCE = [ABC for ABC in TEST_SEED]

class TestShuffle(unittest.TestCase):
    def test_shuffle_list(self):
        sequence = shuffle(TEST_SEQUENCE, TEST_SEED)
        self.assertEqual(
            sequence,
            ['c', 'P', 'o', 's', 'y', 's', 'a']
        )
        return sequence

    def test_unshuffle_list(self):
        sequence = unshuffle(self.test_shuffle_list(), TEST_SEED)
        self.assertEqual(
            sequence,
            TEST_SEQUENCE
        )

if __name__ == '__main__':
    unittest.main()
