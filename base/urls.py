from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # Here first paramter is path, 2nd one is views function name and 3rd one a name for the path 
    # We can use 3rd paramter i.e 'name' to reference the url from some other page.
    path('room/<str:pk>/', views.room, name="room") 
]