import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

from e_commerce.stores.models import Category, Product

pytestmark = pytest.mark.django_db


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "django")


class TestProductsModel(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        # User.objects.create(username='admin')
        Category.objects.create(name="django", slug="django")
        id_dj = Category.objects.only("id").get(name="django").id
        self.data1 = Product.objects.create(
            category_id=id_dj,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        # self.data2 = Product.products.create(category_id=1, title='django advanced', created_by_id=1,
        #                                      slug='django-advanced', price='20.00', image='django', is_active=False)

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")
