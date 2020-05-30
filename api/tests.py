from django.test import TestCase


from books import models


# Create your tests here.

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Book.objects.create(title='Yoga', subtitle='Phycology', author='Safronov A', isbn='321 654654987')

    def test_title_content(self):
        book = models.Book.objects.last()
        expected_object_name = f'{book.title}'
        self.assertEquals(expected_object_name, 'Yoga')

    def test_body_content(self):
        book = models.Book.objects.last()
        expected_object_name = f'{book.author}'
        self.assertEquals(expected_object_name, 'Safronov A')

