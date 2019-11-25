from django.urls import path

from . import views
from .views import SearchResultsView

app_name = 'alumnos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('nuevo/', views.PostView, name='post'),
    path('nuevo/archivo', views.simple_upload, name='postfile'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]