from django.urls import path
# Views
from apps.users import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(),
        name="login"
    ),
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        "create/",
        views.UserRegisterView.as_view(),
        name="create"
    ),
    path(
        "update/",
        views.UpdatePasswordView.as_view(),
        name="update"
    ),
]

