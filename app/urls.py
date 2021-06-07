from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), 
    path('login_page', views.login_page, name="login_page"),
    path('logout_view', views.logout_view, name="logout_view")
]