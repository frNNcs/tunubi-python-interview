from datetime import datetime
from email.policy import default

from marshmallow import fields
from marshmallow import Schema
from marshmallow import validate
from marshmallow import post_load

from .models import Poll
from .models import Answer


class PollsSchema(Schema):
    _id = fields.Str(dump_only=True)
    question = fields.Str(required='Question is required',
                          validate=[
                              validate.Length(
                                  min=1,
                                  error='Question cannot be empty')
                          ])
    created_at = fields.DateTime()

    @post_load
    def make_poll(self, data, **kwargs):
        return Poll(**data)


class AnswersSchema(Schema):
    _id = fields.Str(dump_only=True)
    answer = fields.Str(required='Answer is required',
                        validate=[
                            validate.Length(
                                min=1,
                                error='Answer cannot be empty')
                        ])
    created_at = fields.DateTime()
    poll_id = fields.Str()

    @post_load
    def make_poll(self, data, **kwargs):
        return Answer(**data)
