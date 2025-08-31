from rest_framework import serializers
from accounts.models.User import User
from accounts.exceptions.user_exception import UserException
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        request = self.context.get("request")
        method = request.method if request else None

        if not username or not email or not password:
            raise UserException.InvalidUserCredentials()

        if method == "POST":
            if (
                User.objects.filter(username=username).exists()
                or User.objects.filter(email=email).exists()
            ):
                raise UserException.UserAlreadyExists()

        if method in ["PUT", "PATCH"] and self.instance:
            if (
                User.objects.exclude(pk=self.instance.pk)
                .filter(username=username)
                .exists()
                or User.objects.exclude(pk=self.instance.pk)
                .filter(email=email)
                .exists()
            ):
                raise UserException.UserAlreadyExists()
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        password = validated_data.get("password")
        if password:
            instance.password = make_password(password)
        instance.save()
        return instance
