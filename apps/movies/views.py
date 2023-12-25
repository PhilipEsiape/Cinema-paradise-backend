from rest_framework import generics, filters
from .serializer import MovivesSerializer
from .models import Movies
from django_filters.rest_framework import DjangoFilterBackend

class MoviesList(generics.ListAPIView):
  queryset = Movies.objects.order_by('-created_at').all()
  serializer_class = MovivesSerializer
  filter_backens = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['category_id', 'realease_type']
  search_fields = ['name', 'description']

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serilizer_class = MovivesSerializer


  

