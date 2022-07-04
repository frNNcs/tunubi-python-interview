import bson

from marshmallow import fields
from marshmallow import Schema
from marshmallow import validate
from marshmallow import post_load
from marshmallow import ValidationError

from .models import Poll
from .models import Answer


class ObjectId(fields.Field):
    """
    Marshmallow field for :class:`bson.ObjectId`
    """

    def _serialize(self, value, *args, **kwargs):
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value, *args, **kwargs):
        try:
            return bson.ObjectId(value)
        except (TypeError, bson.errors.InvalidId):
            raise ValidationError('Invalid ObjectId.')


class PollsSchema(Schema):
    _id = ObjectId()
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
    _id = ObjectId()
    answer = fields.Str(required='Answer is required',
                        validate=[
                            validate.Length(
                                min=1,
                                error='Answer cannot be empty')
                        ])
    created_at = fields.DateTime()
    poll_id = ObjectId()

    @post_load
    def make_poll(self, data, **kwargs):
        return Answer(**data)
