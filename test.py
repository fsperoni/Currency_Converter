from unittest import TestCase
from app import app
from helpers import is_valid_amount,  is_valid_currency


class FlaskTests(TestCase):

    def setUp(self):
        """To be done before every test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
    
    def test_homepage(self):
        """Make sure home page is loaded with the conversion form."""

        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"<h4>Select the currencies", response.data)
            self.assertIn(b"Amount:", response.data)
            self.assertIn(b"Convert", response.data)
    
    def test_valid_currency(self):
        """Test for valid currency"""
        self.assertEqual(is_valid_currency("USD"), True)
        self.assertEqual(is_valid_currency("EUR"), True)
        self.assertEqual(is_valid_currency("ABC"), False)
    
    def test_valid_amount(self):
        """Test for valid amount"""
        self.assertEqual(is_valid_amount("123.58999"), True)
        self.assertEqual(is_valid_amount("abcde"), False)
        self.assertEqual(is_valid_amount("-10.35"), False)

    def test_conversion(self):
        """Make sure conversion between same currencies is working."""

        with app.test_client() as client:

            response = client.post("/convert", data={"fromCurrency": "USD", "toCurrency": "USD", "amount": "100"})
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("Converting US$100.00 (USD-United States dollar) leads to \n  US$100.00 (USD-United States dollar).", html)