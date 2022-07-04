from flask import request
from flask import json
from flask import Response
from flask import Blueprint

from config import MongoAPI

polls_bp = Blueprint('polls', __name__, url_prefix='/')


@polls_bp.route('/')
def base():
    return "status:up"


@polls_bp.route('/answer_poll/', methods=['POST'])
def answer_poll():
    data = request.json
    res = MongoAPI("answers").write(data)
    return Response(response=json.dumps(res),
                    status=200,
                    mimetype='application/json')


@polls_bp.route('/polls/', methods=['POST'])
def create_poll():
    data = request.json
    res = MongoAPI("polls").write(data)
    return Response(response=json.dumps(res),
                    status=200,
                    mimetype='application/json')


@polls_bp.route('/polls/', methods=['GET'])
def get_all_polls():
    polls = MongoAPI("polls").read()
    answers = MongoAPI("answers").read()
    for poll in polls:
        poll['answers'] = [
            answer for answer in answers if answer['poll_id'] == poll['_id']]
    return Response(response=json.dumps(polls))
