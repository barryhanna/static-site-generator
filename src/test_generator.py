import unittest

from generator import extract_title


class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        actual = extract_title(
            "# This is the title\nThen some other markdown stuff")
        expected = "This is the title"
        self.assertEqual(actual, expected)

    def test_extract_title_missing_raises_exception(self):
        self.assertRaises(Exception, extract_title,
                          "This is the title\nThen some other markdown stuff")


if __name__ == "__main__":
    unittest.main()
