from datetime import datetime

from django.test import TestCase
from csopen.core.models import Supplier


class SupplierModelTest(TestCase):
    def setUp(self):
        self.obj = Supplier(
          code=1,
          company='Emerson Henning ME',
          trade='Henning Informática',
          cnpj='00000000000000',
          observation='Alguma observação.'
      )


    def test_create(self):
      self.obj.save()
      self.assertTrue(Supplier.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)