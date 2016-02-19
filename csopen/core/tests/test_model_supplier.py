from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase
from csopen.core.models import Supplier



class SupplierModelTest(TestCase):
    def setUp(self):
        self.obj = Supplier(
          code=1,
          company='Emerson Henning ME',
          trade='Henning Informática',
          cnpj='00000000000000',
          observations='Alguma observação.'
      )


    def test_create(self):
        self.obj.save()
        self.assertTrue(Supplier.objects.exists())

    def test_created_at(self):
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_supplier_code_cannot_repeat(self):
        ''' The code can not be repeated '''
        supplier2 = Supplier(
          code=1,
          company='XX',
          trade='XXXX',
          cnpj='00000000000000',
          observations='Alguma observação.')

        self.obj.save()
        self.assertRaises(IntegrityError, supplier2.save)