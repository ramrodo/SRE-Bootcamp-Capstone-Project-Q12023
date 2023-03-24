""" Unit tests for the login module. """
import unittest
from api.login import Token, Restricted

TOKEN = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
        "eyJyb2xlIjoiYWRtaW4ifQ."
        "BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w"
        )

class TestApiMethods(unittest.TestCase):
    """ Tests for api methods. """

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        """ Test the generation of the token. """
        username = "admin"
        password = "secret"

        self.assertEqual(TOKEN, self.convert.generate_token(
            username, password))

if __name__ == "__main__":
    unittest.main()
