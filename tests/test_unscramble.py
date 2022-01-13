import unittest
import json
import os

from pycasso import Canvas

TEST_IMAGE = os.path.join(os.path.dirname(__file__), "data/test_image.jpg")
TEST_INPUT = os.path.join(os.path.dirname(__file__), "data")
TEST_OUTPUT = os.path.join(os.path.dirname(__file__), "output")
TEST_SLICE_SIZE = (50, 50)
TEST_SEED = "Pycasso"

class TestExport(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(
            TEST_IMAGE,
            TEST_SLICE_SIZE,
            TEST_SEED
        )

    def tearDown(self):
        for file in os.listdir(TEST_OUTPUT):
            os.remove(os.path.join(TEST_OUTPUT, file))
        os.rmdir(TEST_OUTPUT)

    def test_export_scramble(self):
        self.canvas.export(
            "scramble",
            f"{TEST_OUTPUT}/test_scramble",
            "png"
        )
        self.assertTrue(
            os.path.exists(f"{TEST_OUTPUT}/test_scramble.png")
        )

    def test_export_unscramble(self):
        self.canvas.export(
            "unscramble",
            f"{TEST_OUTPUT}/test_unscramble",
            "png"
        )
        self.assertTrue(
            os.path.exists(f"{TEST_OUTPUT}/test_unscramble.png")
        )

    def test_export_jpeg(self):
        self.canvas.export(path = f"{TEST_OUTPUT}/test", format = "jpeg")
        self.assertTrue(
            os.path.exists(f"{TEST_OUTPUT}/test.jpeg")
        )

    def test_export_bmp(self):
        self.canvas.export(path = f"{TEST_OUTPUT}/test", format = "bmp")
        self.assertTrue(
            os.path.exists(f"{TEST_OUTPUT}/test.bmp")
        )

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(
            TEST_IMAGE,
            TEST_SLICE_SIZE,
            TEST_SEED
        )
        self.slices = self.canvas.get_slices()

    def tearDown(self):
        self.canvas.close()

    def test_get_slices(self):
        with open(f"{TEST_INPUT}/test_get_slices.json", 'r') as file:
            slice = file.read()
            slice = json.loads(slice)
        self.assertEqual(self.slices, slice)

    def test_get_group(self):
        group = [self.canvas.get_group(self.slices[i]) for i in self.slices]

        self.assertEqual(
            group,
            [
              {
                "slices": 100,
                "cols": 10,
                "rows": 10.0,
                "width": 500,
                "height": 500.0,
                "x": 0,
                "y": 0
              },
              {
                "slices": 10,
                "cols": 1,
                "rows": 10.0,
                "width": 40,
                "height": 500.0,
                "x": 500,
                "y": 0
              },
              {
                "slices": 10,
                "cols": 10,
                "rows": 1.0,
                "width": 500,
                "height": 8.0,
                "x": 0,
                "y": 500
              },
              {
                "slices": 1,
                "cols": 1,
                "rows": 1.0,
                "width": 40,
                "height": 8.0,
                "x": 500,
                "y": 500
              }
            ]
        )

    def test_get_cols_in_group(self):
        cols = [self.canvas.get_cols_in_group(self.slices[i]) for i in self.slices]

        self.assertEqual(cols, [10, 1, 10, 1])

if __name__ == '__main__':
    unittest.main()
