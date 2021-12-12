from django.urls import path
# views
from apps.carts import views

app_name = "carts"

urlpatterns = [
    path(
        'cart/add/',
        views.CartAdd.as_view(),
        name="add"
    ),
]
