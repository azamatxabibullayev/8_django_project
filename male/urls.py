from django.urls import path
from male.views import male

urlpatterns = [
    path('male', male)
]
