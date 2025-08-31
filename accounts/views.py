from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models.User import User
from accounts.serializers.user_serializer import UserSerializer
from accounts.exceptions.user_exception import UserException


class UserViews(APIView):
    class CreateUserView(APIView):
        def post(self, request):
            serializer = UserSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                user = serializer.create(serializer.validated_data)
                return Response(
                    UserSerializer(user).data, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class ListUsersView(APIView):
        def get(self, request):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    class RetrieveUserView(APIView):
        def get(self, request, pk):
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise UserException.UserNotFound()
            serializer = UserSerializer(user)
            return Response(serializer.data)

    class UpdateUserView(APIView):
        def put(self, request, pk):
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise UserException.UserNotFound()
            serializer = UserSerializer(
                user, data=request.data, context={"request": request}
            )
            if serializer.is_valid():
                user = serializer.update(user, serializer.validated_data)
                return Response(UserSerializer(user).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class DeleteUserView(APIView):
        def delete(self, request, pk):
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise UserException.UserNotFound()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    class GetUserByEmailView(APIView):
        def get(self, request):
            email = request.query_params.get("email")
            if not email:
                return Response(
                    {"error": "Email não informado."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise UserException.UserNotFound()
            serializer = UserSerializer(user)
            return Response(serializer.data)
