from django.urls import path
from . import views

urlpatterns = [

    path('food/', views.read, name="food"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"), 

]