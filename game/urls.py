from django.urls import path
from . import views
urlpatterns  = [
    path('', views.index, name= 'home'),
    path('we', views.my, name= 'my'),
]
