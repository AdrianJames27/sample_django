from django.urls import path
from . import views


# if wildcard /<int:user_id>/
# in the views.py view(request, user_id)
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected')
]
