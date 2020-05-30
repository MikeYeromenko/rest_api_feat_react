from rest_framework.generics import ListAPIView
from rest_framework import viewsets


from api import serializers
from books import models


class BookAPIView(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
