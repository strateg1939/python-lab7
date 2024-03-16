import unittest


import unittest
import os
import pandas as pd

from app.io.input import get_text_from_file, get_text_from_file_using_pandas

class TestGetTextFromFile(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_file.txt'
        self.empty_test_file_path = 'empty_file.txt'
        with open(self.test_file_path, 'w') as file:
            file.write("This is a test file.\nIt contains some text.")
        with open(self.empty_test_file_path, 'w') as file:
            file.write("")

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.empty_test_file_path):
            os.remove(self.empty_test_file_path)

    def test_get_text_from_file_success(self):
        expected_text = "This is a test file.\nIt contains some text."
        text = get_text_from_file(self.test_file_path)
        self.assertEqual(text, expected_text)

    def test_get_text_from_file_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            get_text_from_file('nonexistent_file.txt')

    def test_get_text_from_file_empty_file(self):
        expected_text = ""
        text = get_text_from_file(self.empty_test_file_path)
        self.assertEqual(text, expected_text)


class TestGetTextFromFileUsingPandas(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_file.tsv'
        self.empty_test_file_path = 'empty_file.tsv'
        data = pd.DataFrame({'text': ["This is a test file.", "It contains some text."]})
        data.to_csv(self.test_file_path, sep='\t', index=False, header=False)
        with open(self.empty_test_file_path, 'w') as file:
            file.write("")

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.empty_test_file_path):
            os.remove(self.empty_test_file_path)

    def test_get_text_from_file_using_pandas_success(self):
        expected_text = "This is a test file. It contains some text."
        text = get_text_from_file_using_pandas(self.test_file_path)
        self.assertEqual(text, expected_text)

    def test_get_text_from_file_using_pandas_nonexistent_file(self):
        expected_text = "File not found"
        text = get_text_from_file_using_pandas("no_file.tsv")
        self.assertEqual(text, expected_text)

    def test_get_text_from_file_using_pandas_empty_file(self):
        empty_file_path = self.empty_test_file_path
        pd.DataFrame().to_csv(empty_file_path, sep='\t', index=False, header=False)
        with self.assertRaises(ValueError):
            get_text_from_file_using_pandas(empty_file_path)


if __name__ == '__main__':
    unittest.main()
