from rest_framework.exceptions import APIException
from rest_framework import status

class UserException():
    
    class UserNotFound(APIException):
        status_code = status.HTTP_404_NOT_FOUND
        default_detail = 'Usuario não encontrado.'
        default_code = 'user_not_found'
        
    class UserAlreadyExists(APIException):
        status_code = status.HTTP_400_BAD_REQUEST
        default_detail = 'Usuario já existe.'
        default_code = 'user_already_exists'
        
    class InvalidUserCredentials(APIException):
        status_code = status.HTTP_401_UNAUTHORIZED
        default_detail = 'Dados inválidos para cadastro/edição de usuário.'
        default_code = 'invalid_user_credentials'