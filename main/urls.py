from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth, name='auth'),
    path('profile', views.profile, name='profile'),
    path('mobile', views.mobile, name='mobile'),
    path('sign_out', views.sign_out, name='sign_out')

]
