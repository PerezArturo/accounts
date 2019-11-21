from django.urls import path

from . import views

app_name = 'grupos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('nuevo/', views.PostView, name='post'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
]