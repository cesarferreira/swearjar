import unittest
from unittest.mock import patch, mock_open
import swearjar

class TestSwearJar(unittest.TestCase):

    fake_swear_words = ['fakebadword1', 'fakebadword2']
    test_data = "This is a test line with fakebadword1.\nThis is a clean line.\nAnother fakebadword2 here.\n"

    def setUp(self):
        self.test_data = TestSwearJar.test_data

    @patch('swearjar.load_swear_words', return_value=fake_swear_words)
    @patch('builtins.open', new_callable=mock_open, read_data=test_data)
    def test_find_swear_words(self, mock_file, mock_load_swear_words):
        # Test finding swear words in a file
        matches_found = swearjar.find_swear_words('fake_file_path', TestSwearJar.fake_swear_words)
        self.assertEqual(matches_found, 2)

    @patch('swearjar.load_swear_words', return_value=fake_swear_words)
    @patch('builtins.open', new_callable=mock_open, read_data="This is a clean line with no swear words.\n")
    def test_find_swear_words_no_swear_words(self, mock_file, mock_load_swear_words):
        # Test finding swear words in a file when there are no swear words
        matches_found = swearjar.find_swear_words('fake_file_path', TestSwearJar.fake_swear_words)
        self.assertEqual(matches_found, 0)

if __name__ == '__main__':
    unittest.main()