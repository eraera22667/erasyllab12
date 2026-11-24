from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("decrease/<int:pk>/", views.decrease_stock, name="decrease_stock"),
]
