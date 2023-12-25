from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.order_by('-created_at').all()
    serializer_class = CategorySerializer



  
