from flask import Blueprint

log_in = Blueprint('log_in', __name__)


# this is the home route.
# it redirects to the main log in route
@log_in.route('/', methods=['GET'])
def home():
    return '<h1>Home</h1>'


# main log in route (contains three buttons to redirect to login types)
@log_in.route('/log_in', methods=['GET'])
def log_in_main():
    return '<h1>Login Main</h1>'


# takes log in type as part of url (pilots/customers/representatives)
# determines which table to look at for name + id
@log_in.route('/log_in/<userType>', methods=['GET'])
def pilots(user_type):
    return '<h1>Login ' + user_type + '</h1>'
