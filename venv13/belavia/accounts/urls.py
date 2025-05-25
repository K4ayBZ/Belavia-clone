from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('main/', views.main, name='main'),
    path('history/', views.history, name='history'),
    path('fleet/', views.fleet, name='fleet'),
    path('base/', views.base, name='base')
]
