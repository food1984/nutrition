import unittest
from mock import patch
from get_govt_data.get_govt_data import (convert_boolean, cleanup)


class TestGovtData(unittest.TestCase):
    def test_convert_boolean_no(self):
        self.assertEqual(False, convert_boolean('N'))
        self.assertEqual(False, convert_boolean('No'))
        self.assertEqual(False, convert_boolean('n'))
        self.assertEqual(False, convert_boolean('no'))
        self.assertEqual(False, convert_boolean('NO'))

    def test_convert_boolean_yes(self):
        self.assertEqual(True, convert_boolean('Y'))
        self.assertEqual(True, convert_boolean('y'))
        self.assertEqual(True, convert_boolean('Yes'))
        self.assertEqual(True, convert_boolean('YES'))
        self.assertEqual(True, convert_boolean('yes'))

    @patch('get_govt_data.get_govt_data.logging')
    def test_cleanup_successful(self, mock_logging):
        test_dir = 'test'
        cleanup(test_dir)
        mock_logging.info.assert_called_with('Successfully cleaned, {}'.
                                             format(test_dir))

    @patch('get_govt_data.get_govt_data.logging')
    def test_cleanup_directory_exists(self, mock_logging):
        test_dir = 'test'
        self.assertRaises(FileExistsError, cleanup(test_dir))
        mock_logging.info.assert_called_with('Successfully cleaned, {}'.
                                             format(test_dir))

    @patch('get_govt_data.get_govt_data.logging')
    def test_cleanup_no_files(self, mock_logging):
        test_dir = 'test'
        self.assertRaises(FileNotFoundError, cleanup(test_dir))
        mock_logging.info.assert_called_with('Successfully cleaned, {}'.
                                             format(test_dir))


if __name__ == '__main__':
    unittest.main()
