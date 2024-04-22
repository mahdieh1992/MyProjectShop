from django.urls import path
from .views import RegisterUserGeneric

app_name='account_api'

urlpatterns = [
    path('register/',RegisterUserGeneric.as_view(),name='register')
    
]