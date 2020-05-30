from django.urls import path, include
from rest_framework import routers

from api import resources


router = routers.DefaultRouter()
router.register('books', resources.BookAPIView)


urlpatterns = [
    path('', include(router.urls)),
]
