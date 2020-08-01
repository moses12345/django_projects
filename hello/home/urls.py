from django.contrib import admin
from django.urls import path,include
from home import views
#understood url dispatching
urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact")
    
]