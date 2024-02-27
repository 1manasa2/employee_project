from django.contrib import admin
from django.urls import path
from . import views
urlpatterns= (
    path('',views.index,name='index'),
    path('display/',views.display,name='display'),
    path('insert/',views.insert,name='insert'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
)