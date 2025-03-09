from django.urls import path
from . import views
from .models import Artist

# path('', views., name=''),

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('artists/', views.artists, name='artists'),
]

