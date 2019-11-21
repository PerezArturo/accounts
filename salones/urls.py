from django.urls import path

from . import views

app_name = 'salones'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('nuevo/', views.PostView, name='post'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
]