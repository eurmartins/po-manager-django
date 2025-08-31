from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db import IntegrityError
from accounts.exceptions.user_exception import UserException

def user_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, UserException.UserAlreadyExists):
        return Response({"error": exc.detail}, status=exc.status_code)
    if isinstance(exc, UserException.UserNotFound):
        return Response({"error": exc.detail}, status=exc.status_code)
    if isinstance(exc, UserException.InvalidUserCredentials):
        return Response({"error": exc.detail}, status=exc.status_code)
    
    if isinstance(exc, IntegrityError):
        return Response(
            {"error": UserException.UserAlreadyExists.default_detail},
            status=UserException.UserAlreadyExists.status_code,
        )

    if response is not None:
        response.data["custom_message"] = "Ocorreu um erro, revise sua requisição!"
        if response.status_code == 400:
            response.data["custom_message"] = "Dados inválidos."
    return response