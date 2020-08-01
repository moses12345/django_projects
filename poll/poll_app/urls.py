from django.contrib import admin
from django.urls import path,include
from poll_app import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('vote/<poll_id>/',views.vote,name='vote'),
    path('result/<poll_id>/',views.result,name='result'),
    

]