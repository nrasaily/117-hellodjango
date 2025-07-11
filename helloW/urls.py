from django.urls import path
from helloW import views 

urlpatterns = [
  path('', views.home, name='home'),
]