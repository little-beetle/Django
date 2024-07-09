from django.urls import path
from . import views

app_name = 'happy_day'

urlpatterns = [
    path('', views.day_index, name='index'),
    path('postcard/', views.postcard, name='postcard'),
    path('greeting/', views.greeting, name='greeting'),
    path('win/', views.win, name='win'),

]
