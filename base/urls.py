from django.urls import path
from .views import policy
urlpatterns = [
    path('', policy),
]
