from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=(
    path('',views.index,name='index'),
    path('addRooms/',views.addRooms,name='addRooms'),
    path('BookRoom/',views.BookRoom,name='BookRoom'),
    path('disproomdet/',views.disproomdet,name='disproomdet'),
)
