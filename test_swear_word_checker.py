import unittest
from unittest.mock import patch, mock_open
import swearcheck

class TestSwearWordChecker(unittest.TestCase):

    def setUp(self):
        # Setup any repeated used variables or mock data here
        self.swear_words = ['badword1', 'badword2']
        self.test_data = "This is a test line with badword1.\nThis is a clean line.\nAnother badword2 here.\n"

    @patch('swear_word_checker.open', new_callable=mock_open, read_data="badword1\nbadword2\n")
    def test_load_swear_words(self, mock_file):
        # Test loading swear words from file
        result = swear_word_checker.load_swear_words('fake_path')
        self.assertEqual(result, self.swear_words)

    @patch('swear_word_checker.open', new_callable=mock_open, read_data=test_data)
    def test_find_swear_words(self, mock_file):
        # Test finding swear words in a file
        with patch('builtins.print') as mock_print:
            swear_word_checker.find_swear_words('fake_path', self.swear_words)
            mock_print.assert_called_with('fake_path:3: Another \x1b[1mbadword2\x1b[0m here.')

if __name__ == '__main__':
    unittest.main()
