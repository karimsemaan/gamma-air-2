from flask import Blueprint

log_in = Blueprint('log_in', __name__)


# this is the home route.
# has three buttons to redirect to the right login paths
@log_in.route('/', methods=['GET'])
def home():
    return '<h1>Home</h1>'


# takes log in type as part of url (pilots/customers/representatives)
# determines which table to look at for name + id
@log_in.route('/log_in/<userType>', methods=['GET'])
def log_in_specific(userType):
    return '<h1>Login ' + userType + '</h1>'
