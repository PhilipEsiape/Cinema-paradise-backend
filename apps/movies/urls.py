from django.urls import path
from .import views


urlpatterns = [
    path('', views.MoviesList.as_view(), name='movies'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie_detail')
]