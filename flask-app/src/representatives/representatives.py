from flask import Blueprint, request, jsonify, current_app
from src import execute_query
import src.log_in as user_info

reps = Blueprint('reps', __name__)


# ANSWERING QUESTIONS #


# Displays all questions asked by customers that this representative is assigned to.
# Doesn't display questions that are already answered.
@reps.route('/view-questions', methods=['GET'])
def view_questions():
    query = '''select id, question, isResolved from 
        (select id as customer from Customers where supportRep = {0}) c natural join Questions
        order by isResolved
        '''
    data = execute_query(query.format(user_info.current_user_id))
    return jsonify(data)


@reps.route('/view-question/<questionID>', methods=['GET'])
def view_specific_question(questionID):
    query = '''
        select question, response, firstName, lastName
        from (select * from Questions where id = {}) q
                 join Customers c on q.customer = c.id
    '''.format(questionID)
    data = execute_query(query)
    current_app.logger.info(query)

    return data


# Submits an answer to the database and redirects back to the '/answer-questions' route.
@reps.route('/submit-answer/<questionID>', methods=['POST'])
def submit_answer(questionID):
    response = request.args.to_dict().get("response")
    query = '''update Questions 
        set response = '{0}', isResolved = true, customerRep = {1}
        where id = {2}
        '''.format(response, user_info.current_user_id, questionID)
    execute_query(query, True)
    return 'Success'
