from django.urls import path, include
from knox import views as knox_views
from .views import *

urlpatterns = [
    path('lot-list/', CharityLotsList.as_view()),
    path('bids/', CharityBidsList.as_view()),

    path('auth/login/', AuthLoginView.as_view()),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/info/', UserInfoView.as_view()),
]
