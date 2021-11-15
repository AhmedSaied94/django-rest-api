from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


app_name = 'accounts'
router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('users', start, name='start'),
    path('signup', signup, name='signup'),
    path('<str:un>/details', user_details, name='user-details'),
    path('details', user_details, name='my-details'),
    path('delete', delete_user, name='user-delete'),
    path('update', user_update, name='user-update'),
    path('login', obtain_auth_token, name='login'),
    path('logout', logout, name='logout')

]