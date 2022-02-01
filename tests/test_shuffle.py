import unittest
import pytest

from pycasso import shuffle, unshuffle


@pytest.mark.usefixtures("fixtures_class")
class TestShuffle(unittest.TestCase):
    def test_shuffle_list(self):
        sequence = shuffle(
            [abc for abc in self.params.seed],
            self.params.seed
        )
        self.assertEqual(
            sequence,
            ['c', 'P', 'o', 's', 'y', 's', 'a']
        )
        return sequence

    def test_unshuffle_list(self):
        sequence = unshuffle(
            self.test_shuffle_list(),
            self.params.seed
        )
        self.assertEqual(
            sequence,
            [abc for abc in self.params.seed]
        )


if __name__ == '__main__':
    unittest.main()
