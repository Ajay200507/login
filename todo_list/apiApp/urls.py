from django.urls import path
import apiApp.views as v

urlpatterns = [
    path('login',v.login,name='login'),
    path('create_user',v.create_user,name='create_user')
]