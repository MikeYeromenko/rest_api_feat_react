from rest_framework.serializers import ModelSerializer

from books import models


class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'subtitle', 'author', 'isbn']
