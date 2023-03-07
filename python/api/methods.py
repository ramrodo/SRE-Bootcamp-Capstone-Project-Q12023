""" Methods for Login module. """
import hashlib
import jwt

class Token:
    """ Class to handle the token for authentication. """

    def generate_token(self, username, password, query_data):
        """ Generates a JWT token with the data given. """
        encrypt_token = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

        user_salt = query_data[0]
        user_password = query_data[1]
        user_role = query_data[2]

        if username is not None and password is not None:
            hashed_password = hashlib.sha512(
                (password + user_salt).encode()).hexdigest()

            if hashed_password == user_password:
                jwt_token = jwt.encode({ "role": user_role }, encrypt_token, algorithm='HS256')
                return jwt_token
            return False

        return False

class Restricted:
    """ Class to handle the protected data. """

    def access_data(self, authorization):
        """ Verifies and authorize the access to the data. """
        try:
            data_decoded = jwt.decode(
                authorization.replace('Bearer', '')[1:],
                'my2w7wjd7yXF64FIADfJxNs1oupTGAuW',
                algorithms='HS256'
            )
        except jwt.ExpiredSignatureError as exception:
            return exception

        if 'role' in data_decoded:
            return True

        return False
