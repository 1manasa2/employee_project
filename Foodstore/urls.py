from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=(
    path('',views.index,name='index'),
    path('addfooditem/',views.addfooditem,name='addfooditem'),
    path('displayitems/',views.displayitems,name='displayitems')
)