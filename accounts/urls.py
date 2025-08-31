from django.urls import path

from .views import UserViews

CreateUserView = UserViews.CreateUserView
ListUsersView = UserViews.ListUsersView
RetrieveUserView = UserViews.RetrieveUserView
UpdateUserView = UserViews.UpdateUserView
DeleteUserView = UserViews.DeleteUserView
GetUserByEmailView = UserViews.GetUserByEmailView

urlpatterns = [
    path("users/create-user/", CreateUserView.as_view(), name="create-user"),
    path("users/list/", ListUsersView.as_view(), name="list-users"),
    path("users/<int:pk>/", RetrieveUserView.as_view(), name="retrieve-user"),
    path("users/update/<int:pk>/", UpdateUserView.as_view(), name="update-user"),
    path("users/delete/<int:pk>/", DeleteUserView.as_view(), name="delete-user"),
    path("users/by-email/", GetUserByEmailView.as_view(), name="get-user-by-email"),
]
