# These functions need to be implemented
from database import validateUser, get_user_role_by_token
import jwt
import os

token = None


class Token:

    def generate_token(self, username, password):
        global token
        if validateUser(username, password):
            userrole = get_user_role_by_token(username)[0]
            payload = {'role': str(userrole)}
            secret = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
            token = jwt.encode(payload, secret, algorithm='HS256')
            os.environ['TOKEN'] = token
            return token
        else:
            return 'HttpError', 403


class Restricted:

    def access_data(self, authorization):
        global token
        secret_key = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
        current_role = jwt.decode(jwt=authorization, algorithms='HS256', verify=True, key=secret_key)
        if current_role['role'] == 'admin':
            message = "You are under protected data"
        else:
            message = "you are not under protected data"

        return message
