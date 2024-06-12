"""
Author- Suraj Prakash Patil
Date- 11/06/2024

"""


from functools import wraps
from flask import request, abort

def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == 'admin' and auth.password == 'secret'):
            abort(401)
        return f(*args, **kwargs)
    return decorated

