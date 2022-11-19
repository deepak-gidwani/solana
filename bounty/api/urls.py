from django.urls import path
from . import views


urlpatterns = [
    path('',views.getElements,name="getElements"),
    path('addElements/',views.addElements,name="addElements"),
]
