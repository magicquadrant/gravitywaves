from protorpc import messages
from google.appengine.ext import ndb


class Session(ndb.Model):
    """Session -- Session object"""
    name = ndb.StringProperty()


class SessionForm(messages.Message):
    """Session -- Session outbound form message"""
    name = messages.StringField(1)


class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    data = messages.StringField(1, required=True)
