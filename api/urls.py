from django.urls import path, include
from .views import *

urlpatterns = [
    path('lot-list/', CharityLotsList.as_view()),
]
