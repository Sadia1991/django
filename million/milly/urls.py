from . import views
from django.urls import path

# app_name = 'myview'

urlpatterns = [
    path('', views.myview, name='myview'),
    path('edit/', views.myedit, name='myedit'),
]
