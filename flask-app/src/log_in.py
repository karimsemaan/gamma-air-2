from flask import Blueprint, request
from src import db, execute_query

log_in = Blueprint('log_in', __name__)

# handles mapping userType to the appropriate table name
tableMap = {
    "pilots": "Pilots",
    "customers": "Customers",
    "representatives": "CustomerRep",
}

current_user_type = False
current_user_id = -1


# takes log in type as part of url (pilots/customers/representatives)
# determines which table to look at for name + id
@log_in.route('/log_in', methods=['GET'])
def submit_log_in():
    args = request.args.to_dict()
    query = 'select * from ' + tableMap.get(args['userType'], "BAD_TABLE_NAME") \
            + ' where id == ' + args['id'] + ' and lastName == ' + args['name']
    print(query)
    json_data = execute_query(query)

    if len(json_data) > 0:
        current_user_type = tableMap.get(args['userType'], "BAD_TABLE_NAME")
        current_user_id = args['userID']
        return True

    return False


@log_in.route('/get_user_name', methods=['GET'])
def get_user_name():
    return "shai"
