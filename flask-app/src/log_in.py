from flask import Blueprint
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
@log_in.route('/log_in?userType=<userType>&name=<name>&id=<userID>', methods=['GET'])
def submit_log_in(userType, name, userID):
    query = 'select * from ' + tableMap.get(userType, "BAD_TABLE_NAME") \
            + ' where id == ' + userID + ' and lastName == ' + name
    json_data = execute_query(query)

    if len(json_data) > 0:
        current_user_type = userType
        current_user_id = userID
        return True

    return False
