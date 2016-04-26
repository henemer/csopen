from csopen.core.models import Product
from django.db import IntegrityError
from django.test import TestCase
from rest_framework.test import APIClient


class ProductModelTest(TestCase):
    def setUp(self):
        self.obj = Product(
            code='              1',
            description='Produto X',
            unity='PEC',
            cost_price=1.1234,
            profit_margin=0,
            price=1.1234,
            amount=100.555,
            reference='909090',
            max_stock=1000.1234,
            min_stock=1.1234,
            bar_code='7896094910959',
            ncm='',
            observations='Nenhuma observação a ser feita'
      )


    def test_create(self):
        self.obj.save()
        self.assertTrue(Product.objects.exists())

    def test_create_with_only_required_fields(self):
        product = Product(
            code = '1',
            description='Alguma descrição'
        )
        product.save();
        self.assertTrue(Product.objects.exists())


    def test_product_code_cannot_repeat(self):
        ''' The code can not be repeated '''
        product2 = Product(
            code='              1',
            description='Alguma descrição')

        self.obj.save()
        with self.assertRaises(IntegrityError):
            product2.save()

