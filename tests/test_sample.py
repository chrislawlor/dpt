# Place your tests in this directory
# Be sure to prefix module names with "test_"

from django.test import TestCase


class SimpleTest(TestCase):
    def test_addition(self, ):
        result = 2 + 2
        self.assertEqual(4, result)
    
