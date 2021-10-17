import pytest
from django.test import TestCase

from e_commerce.stores.models import Category, Product
from e_commerce.users.models import User

pytestmark = pytest.mark.django_db


class TestCategories(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/type/field attribute
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_default_name(self):
        """
        Test Category model default name
        :return: True or False
        """
        data = self.data1
        self.assertEqual(str(data), "django")


class TestProductsModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_products_model_entry(self):
        """
        Test product model data insertion/type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")
