from rest_framework.exceptions import APIException
from .utils import fail
from rest_framework.response import Response


def exception_handler(exception: Exception, context) -> Response:
    if not isinstance(exception, APIException):
        exception = APIException(str(exception))
        exception.status_code = 500
    return Response(fail(exception.detail), exception.status_code)
