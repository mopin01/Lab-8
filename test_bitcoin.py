import unittest
from unittest import TestCase
from unittest.mock import patch
from bitcoin import bitcoin_to_usd

class TestBitcoin(TestCase):

    @patch('requests.Response.json')
    def test_bitcoin_to_usd(self, mock_requests_json):
        mock_rate = 1000
        mock_response = {
            "bpi": {
                "USD": {
                    "rate_float": mock_rate
                }
            }
        }
        mock_requests_json.return_value = mock_response
        result = bitcoin_to_usd(5)
        expected = 5000
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()