from datetime import datetime

from django.test import TestCase

# Create your tests here.
from order.models import Category, Product


class CategoryTest(TestCase):

    def create_category(self, name="drinks", slug="drinks"):
        return Category.objects.create(name=name, slug=slug)

    def test_category_creation(self):
        obj = self.create_category()
        self.assertTrue(isinstance(obj, Category))


class ProductTest(TestCase):
    def create_product(self):
        category = Category.objects.create(name='drinks', slug="drinks")
        product = Product.objects.create(category=category, name='water', slug='water', available=True,
                                         price=10.87, created=datetime.now)
        return product

    def test_category_creation(self):
        obj = self.create_product()
        self.assertTrue(isinstance(obj, Product))

