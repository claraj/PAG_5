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
        self.assertEqual(update, example, 'When adding a new book author:title, your dictionary was not updated correctly.')


    @patch('builtins.input')
    @patch('builtins.print')
    def test_add_book_already_exists(self, mock_print, mock_input):
        mock_input.side_effect = ['a', 'ccc']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}
        author_book.add_book(example)
        self.assertEqual(update, example, 'When adding a new book author:title, don\'t modify the dictionary if the author is already a key in it.')
        self.assertIn('already in dictionary', all_output(mock_print).lower(), 'Print the message "Already in dictionary" if user tries to add an author that is already in the dictionary')


    @patch('builtins.input')
    def test_edit_book(self, mock_input):
        mock_input.side_effect = ['a', 'asdsdfsdf']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'asdsdfsdf', 'b': 'bbb'}
        author_book.edit_book(example)
        self.assertEqual(update, example, 'When editing a book, the title or author was not modified correctly')


    @patch('builtins.input')
    @patch('builtins.print')
    def test_edit_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c', 'asdsdfsdf']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}
        author_book.edit_book(example)
        self.assertEqual(update, example, 'When trying to edit a book that is not in the dictionary, the dictionary should not be modified')
        self.assertIn('not found', all_output(mock_print).lower(), 'When editing a book that\'s not in the dictionary, print the exact message "Not Found"')


    @patch('builtins.input')
    @patch('builtins.print')
    def test_find_book(self, mock_print, mock_input):
        mock_input.side_effect = ['a']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}

        author_book.find_book(example)
        self.assertEqual(update, example)  # Not modified
        self.assertTrue('aaa' in all_output(mock_print), 'When searching for a book\'s author, print the title for that author if it is found.')


    @patch('builtins.input')
    @patch('builtins.print')
    def test_find_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c', 'whatever']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}

        author_book.find_book(example)
        self.assertEqual(update, example)  # Not modified
        self.assertTrue('not found' in all_output(mock_print).lower(), 'When searching for a book, if the author is not found, print "Not Found"')


    @patch('builtins.input')
    def test_delete_book(self, mock_input):
        mock_input.side_effect = ['a', 'aaa']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'b': 'bbb'}
        author_book.delete_book(example)
        self.assertEqual(update, example, 'When deleting a book, remove the key-value pair where the key matches the author given.')


    @patch('builtins.input')
    @patch('builtins.print')
    def test_delete_book_not_found(self, mock_print, mock_input):
        mock_input.side_effect = ['c', 'something']
        example = {'a': 'aaa', 'b': 'bbb'}
        update = {'a': 'aaa', 'b': 'bbb'}
        author_book.delete_book(example)
        self.assertEqual(update, example, 'When deleting an author that is not in the dictionary, don\'t modify the dictionary')
        self.assertTrue('not found' in all_output(mock_print).lower(), 'When deleting an author that\'s not in the dictionary, print "Not Found')


    @patch('builtins.print')
    def test_view_books(self, mock_print):
        example = {'a': '123', 'b': '456'}
        expected_printed = ['a', '123', 'b', '456']
        author_book.view_books(example)
        self.assertTrue(print_calls_contain_output(mock_print, expected_printed), 'Print all of the authors and titles. Print the authors and titles together.')



