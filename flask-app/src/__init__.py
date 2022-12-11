# Some set up for the application 

from flask import Flask, current_app
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()


def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('../../secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'GammaAir'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Import the various routes
    from src.log_in import log_in
    from src.customers.customers import customers
    from src.representatives.representatives import reps
    from src.pilots.pilots import pilots

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(log_in, url_prefix='/')
    app.register_blueprint(customers, url_prefix='/cust')
    app.register_blueprint(reps, url_prefix='/reps')
    app.register_blueprint(pilots, url_prefix='/pilots')

    return app


def execute_query(query, shouldCommit=False):
    cursor = db.get_db().cursor()
    cursor.execute(query)

    if shouldCommit:
        db.get_db().commit()

    column_headers = [x[0] for x in cursor.description] if not cursor.description is None else []
    data = []

    for row in cursor.fetchall():
        data.append(dict(zip(column_headers, row)))

    return data


def get_next_id(table_name):
    query = '''select max(id) as id from {}'''.format(table_name)
    return int(execute_query(query)[0].get("id")) + 1
