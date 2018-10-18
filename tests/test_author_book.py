from unittest import TestCase
from unittest.mock import patch
from lab_questions import author_book
from tests.print_util import print_calls_contain_output, all_output


class TestAuthorBook(TestCase):
    @patch('builtins.input')
    def test_add_book(self, mock_input):
        mock_input.side_effect = ['c', 'ccc']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}
        author_book.add_book(example)
        self.assertEqual(update, example)


    @patch('builtins.input')
    def test_edit_book(self, mock_input):
        mock_input.side_effect = ['a', 'asdsdfsdf']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'asdsdfsdf', 'b': 'bbb'}
        author_book.edit_book(example)
        self.assertEqual(update, example)


    @patch('builtins.input')
    @patch('builtins.print')
    def test_edit_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c', 'asdsdfsdf']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}
        author_book.edit_book(example)
        self.assertEqual(update, example)
        self.assertIn('Not Found', all_output(mock_print))


    @patch('builtins.input')
    @patch('builtins.print')
    def test_find_book(self, mock_print, mock_input):
        mock_input.side_effect = ['a']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}

        author_book.find_book(example)
        self.assertEqual(update, example)  # Not modified
        self.assertTrue('aaa' in all_output(mock_print))


    @patch('builtins.input')
    @patch('builtins.print')
    def test_find_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}

        author_book.find_book(example)
        self.assertEqual(update, example)  # Not modified
        self.assertTrue('Not Found' in all_output(mock_print))


    @patch('builtins.input')
    def test_delete_book(self, mock_input):
        mock_input.side_effect = ['a']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'b': 'bbb'}
        author_book.delete_book(example)
        self.assertEqual(update, example)


    @patch('builtins.input')
    @patch('builtins.print')
    def test_delete_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}
        author_book.delete_book(example)
        self.assertEqual(update, example)
        self.assertTrue('Not Found' in all_output(mock_print))


    @patch('builtins.print')
    def test_view_books(self, mock_print):
        example = {'a': '123', 'b': '456'}
        expected_printed = ['a', '123', 'b', '456']
        author_book.view_books(example)
        self.assertTrue(print_calls_contain_output(mock_print, expected_printed))



