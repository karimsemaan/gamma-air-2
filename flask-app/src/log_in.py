from flask import Blueprint, request, current_app, jsonify
from src import execute_query

log_in = Blueprint('log_in', __name__)

# handles mapping userType to the appropriate table name
tableMap = {
    "pilots": "Pilots",
    "customers": "Customers",
    "representatives": "CustomerRep",
}

current_user_type = "Customers"
current_user_id = '3696313'


# takes log in type as part of url (pilots/customers/representatives)
# determines which table to look at for name + id
@log_in.route('/log-in', methods=['GET'])
def submit_log_in():
    args = request.args.to_dict()
    query = 'select * from ' + tableMap.get(args['userType'], "BAD_TABLE_NAME") \
            + ' where id = ' + args['id'] + ' and lastName = "' + args['name'] + '"'
    json_data = execute_query(query)

    if len(json_data) > 0:
        global current_user_id, current_user_type
        current_user_type = tableMap.get(args['userType'], "BAD_TABLE_NAME")
        current_user_id = int(args['id'])
        current_app.logger.info(current_user_id)
        return 'Success!'

    return False


@log_in.route('/get-user-name', methods=['GET'])
def get_user_name():
    data = execute_query("select firstName from {0} where id = {1}".format(current_user_type, current_user_id))
    return data[0].get("firstName")
