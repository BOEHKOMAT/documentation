from django.urls import path
from .views import MedicineView, UserView, OrderView


app_name = "Pharmacy"
urlpatterns = [
    path('medicines/', MedicineView.as_view()),
    path('medicines/<int:pk>', MedicineView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>', OrderView.as_view())
]