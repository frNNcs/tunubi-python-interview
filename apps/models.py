from datetime import datetime
from bson import ObjectId


class Poll:
    def __init__(self, question: str, created_at: datetime = None,
                 _id: ObjectId = None):
        self._id = _id
        self.question = question
        self.created_at = created_at if created_at else datetime.now()

    def __dict__(self):
        return {
            "_id": str(self._id),
            "question": self.question,
            "created_at": str(self.created_at)
        }

    def __iter__(self):
        return iter(self.__dict__().items())


class Answer:
    def __init__(self, answer: str, poll_id: ObjectId,
                 created_at: datetime = None, _id: ObjectId = None):
        self._id = _id
        self.answer = answer
        self.created_at = created_at if created_at else datetime.now()
        self.poll_id = poll_id

    def __dict__(self):
        return {
            "_id": str(self._id),
            "answer": self.answer,
            "created_at": str(self.created_at),
            "poll_id": str(self.poll_id)
        }

    def __iter__(self):
        return iter(self.__dict__().items())
