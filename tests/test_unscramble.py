import unittest
import pytest
import json
import os

from pycasso import Canvas

test_input = os.path.join(os.path.dirname(__file__), "data")
test_output = os.path.join(os.path.dirname(__file__), "output")


@pytest.mark.usefixtures("fixtures_class")
class TestExport(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(
            self.params.img_path,
            self.params.slice_size,
            self.params.seed
        )

    def tearDown(self):
        for file in os.listdir(test_output):
            os.remove(os.path.join(test_output, file))
        os.rmdir(test_output)

    def test_export_scramble(self):
        self.canvas.export(
            "scramble",
            "{}/test_scramble".format(test_output),
            "png"
        )
        self.assertTrue(
            os.path.exists("{}/test_scramble.png".format(test_output))
        )

    def test_export_unscramble(self):
        self.canvas.export(
            "unscramble",
            "{}/test_unscramble".format(test_output),
            "png"
        )
        self.assertTrue(
            os.path.exists("{}/test_unscramble.png".format(test_output))
        )

    def test_export_jpeg(self):
        self.canvas.export(
            "scramble",
            "{}/test".format(test_output),
            "jpeg"
        )
        self.assertTrue(
            os.path.exists("{}/test.jpeg".format(test_output))
        )

    def test_export_bmp(self):
        self.canvas.export(
            "scramble",
            "{}/test".format(test_output),
            "bmp"
        )
        self.assertTrue(
            os.path.exists("{}/test.bmp".format(test_output))
        )


@pytest.mark.usefixtures("fixtures_class")
class TestGroup(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(
            self.params.img_path,
            self.params.slice_size,
            self.params.seed
        )
        self.slices = self.canvas.get_slices()

    def tearDown(self):
        self.canvas.close()

    def test_get_slices(self):
        with open("{}/test_get_slices.json".format(test_input), 'r') as file:
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
        cols = [self.canvas.get_cols_in_group(self.slices[i])
                for i in self.slices]

        self.assertEqual(cols, [10, 1, 10, 1])


if __name__ == '__main__':
    unittest.main()
