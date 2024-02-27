from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('displayblog/',views.displayblog,name='displayblog'),
    path('createblog/',views.createblog,name='createblog')
]