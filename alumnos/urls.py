from django.urls import path

from . import views

app_name = 'alumnos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('nuevo/', views.PostView, name='post'),
    path('nuevo/archivo', views.simple_upload, name='postfile'),
    
]