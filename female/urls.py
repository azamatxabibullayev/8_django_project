from django.urls import path
from female.views import female

urlpatterns = [
    path('female', female)
]
