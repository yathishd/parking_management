from django.urls import path

from .views import HomeView,Allparking
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('Search/',views.searchfunction, name='search-result'),
    path('Allparking/',Allparking.as_view(),name='all-parking'),
    path('Signup',views.signupfunction, name='sign-up'),
    path('login',views.loginfunction, name='login'),
    path('logout', views.logoutfunction, name='logout'),
]

