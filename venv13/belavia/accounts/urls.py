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
    path('base/', views.base, name='base'),
    path('base1/', views.base1, name='base1'),
    path('base3/', views.base3, name='base3'),
    path('base4/', views.base4, name='base4'),
    path('base5/', views.base5, name='base5'),
    path('base6/', views.base6, name='base6'),
    path('schedule/', views.schedule, name='schedule'),
]
