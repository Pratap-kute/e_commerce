# import pytest
# from django.test import Client, TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from e_commerce.stores.models import Category, Product
#
# # from e_commerce.users.models import User
#
# pytestmark = pytest.mark.django_db
#
#
# class TestViewResponses(TestCase):
#     def setUp(self):
#         self.c = Client()
#         get_user_model().objects.create_user(
#             username="test", password="12test12", email="test@example.com"
#         )
#         Category.objects.create(name='django', slug='django')
#         id_dj = Category.objects.filter(name='django').values_list('id', flat=True).last()
#         self.data1 = Product.objects.create(
#             category_id=id_dj,
#             title="django beginners",
#             created_by_id=1,
#             slug="django-beginners",
#             price="20.00",
#             image="django",
#         )
#
#     def test_url_allowed_hosts(self):
#         """
#         Test allowed hosts
#         """
#         response = self.c.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_product_detail_url(self):
#         """
#         Test items response status
#         """
#         response = self.c.get(
#             reverse('stores:product_detail', args=['django-beginners']))
#         self.assertEqual(response.status_code, 200)
