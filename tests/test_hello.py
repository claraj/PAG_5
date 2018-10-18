from unittest import TestCase
from lab_questions import hello


class TestHello(TestCase):

    def test_hello(self):
        self.assertEqual('hello', hello.hello().lower(), 'The hello function should return the string "Hello".')
