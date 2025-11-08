# shop/tests.py
from django.test import TestCase
from .models import Product, Order

class ShopTests(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Test", price=10)
        self.assertEqual(product.name, "Test")

    def test_order_creation(self):
        product = Product.objects.create(name="Test2", price=15)
        order = Order.objects.create(product=product)
        self.assertEqual(order.product.name, "Test2")
