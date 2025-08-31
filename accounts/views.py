from rest_framework import viewsets
from .models.User import User
from .serializers.UserSerializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer