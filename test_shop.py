# Unit testing
import unittest
from unittest.mock import patch
from io import StringIO

from shop import *


class ShopTestCase(unittest.TestCase):
    def test_valid_purchase(self):
        with patch('builtins.input', return_value='apple'):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                shop()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Here's your apple!\nYour available money now is £98.50\nThank you for shopping with us. Goodbye!")

    def test_invalid_item(self):
        with patch('builtins.input', side_effect=['invalid', 'exit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                shop()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Invalid input. Please try again.\nThank you for visiting the shop. Goodbye!")

    def test_insufficient_funds(self):
        with patch('builtins.input', side_effect=['red wine', 'exit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                shop()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "You don't have enough money. Do you have more money? Enter the amount:\nThank you for visiting the shop. Goodbye!")

    def test_additional_money(self):
        with patch('builtins.input', side_effect=['red wine', '50', 'exit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                shop()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "You don't have enough money. Do you have more money? Enter the amount:\nYour available money now is £50.00\nThank you for shopping with us. Goodbye!")

    def test_maximum_purchase_attempts(self):
        with patch('builtins.input', side_effect=['red wine', '50', 'cheese', '25', 'milk', '75']):
            with self.assertRaises(MaximumPurchaseAttemptsExceededError):
                shop()

    def test_exit_option(self):
        with patch('builtins.input', return_value='exit'):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                shop()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Thank you for visiting the shop. Goodbye!")


if __name__ == '__main__':
    unittest.main()
