import logging
import endpoints
from protorpc import message_types
from protorpc import remote

from models import Session, SessionForm, StringMessage


@endpoints.api(name='gravitywaves', version='v1')
class GravityWavesApi(remote.Service):
    """gravitywaves API v1."""

    @endpoints.method(
        message_types.VoidMessage,
        StringMessage,
        path='aaa',
        http_method='GET',
        name='aaa'
    )
    def say_hello(self, request):
        """Smile, say Hello!"""
        return StringMessage(data="Hello, have a nice day")

    @endpoints.method(
        SessionForm,
        SessionForm,
        path='bbb',
        http_method='GET',
        name='bbb'
    )
    def error1(self, request):
        """ Demonstrate an Error """
        # the line below will cause an Error
        var1 = request.SessionForm
        logging.info(var1)
        return SessionForm()

    @endpoints.method(
        message_types.VoidMessage,
        SessionForm,
        path='ccc',
        http_method='GET',
        name='ccc'
    )
    def return_session_form(self, request):
        """Return a New SessionForm"""
        sf = SessionForm(name="FooBar")
        return sf


api = endpoints.api_server([GravityWavesApi])
