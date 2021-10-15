"""A SomeController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class SomeController(Controller):
    """SomeController Controller Class."""

    def __init__(self, request: Request):
        """SomeController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view('some', {'world': 'world'})
