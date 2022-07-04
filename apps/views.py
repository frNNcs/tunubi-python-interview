from flask import request
from flask import json
from flask import Response
from flask import Blueprint

from marshmallow import ValidationError

from config import MongoAPI


from .schemas import PollsSchema
from .schemas import AnswersSchema

from .models import Poll
from .models import Answer


polls_bp = Blueprint('polls', __name__, url_prefix='/')


@polls_bp.route('/')
def base():
    return "status:up"


@polls_bp.route('/answer_poll/', methods=['POST'])
def answer_poll():
    try:
        AnswersSchema().load(request.json)
    except ValidationError as err:
        return Response(json.dumps(err.messages),
                        status=400,
                        mimetype='application/json')

    else:
        answer_id = MongoAPI("answers").write(request.json)
        return Response(response=json.dumps({'answer_id': answer_id}),
                        status=200,
                        mimetype='application/json')


@polls_bp.route('/polls/', methods=['POST'])
def create_poll():
    try:
        PollsSchema().load(request.json)
    except ValidationError as err:
        return Response(response=json.dumps(err.messages),
                        status=400,
                        mimetype='application/json')

    else:
        poll_id = MongoAPI("polls").write(request.json)
        return Response(response=json.dumps({'poll_id': poll_id}),
                        status=200,
                        mimetype='application/json')


@polls_bp.route('/polls/', methods=['GET'])
def get_all_polls():
    context = []
    polls = MongoAPI("polls").read()
    answers = MongoAPI("answers").read()

    try:
        for poll in polls:
            _poll = Poll(**poll)
            _aux = dict(_poll)
            _aux.update({"answers": []})
            for ans in answers:
                if ans["poll_id"] == str(_poll._id):
                    _aux["answers"].append(dict(Answer(**ans)))
            context.append(_aux)

    except ValidationError as err:
        return Response(response=json.dumps(err.messages),
                        status=400,
                        mimetype='application/json')
    else:
        return Response(response=json.dumps(context).encode('utf8'),
                        status=200,
                        mimetype='application/json')
