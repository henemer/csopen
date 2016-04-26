from csopen.core.models import Product
from django.test import TestCase
from django_extensions.db.fields import json
from rest_framework.test import APIClient


class ProductModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
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


    def test_post_product(self):
        j = json.dumps({'code':'              1', 'description':'Descrição do Produto'})
        response = self.client.post('/api/produtos/',
                        content_type='application/json',
                        data = j)
        self.assertEqual(response.status_code, 201)


    def test_retrieve_product(self):
        self.obj.save()

        response = self.client.get('/api/produtos/1' )

        self.assertContains(response, 'Produto X')


    def test_update_product(self):
        self.obj.save()

        j = json.dumps({'id':1, 'code':'              22', 'description':'Nova Descrição'})
        response = self.client.put('/api/produtos/1',
                        content_type='application/json',
                        data = j)

        self.assertContains(response, 'Nova Descrição')


    def test_delete_product(self):
        self.obj.save()

        response = self.client.delete('/api/produtos/1')
        self.assertContains(response, 'Ok')


    def test_get_product(self):
        self.obj.save()

        response = self.client.get('/api/produtos/')

        self.assertContains(response, 'Produto X')


    def test_product_code_exists(self):
        self.obj.save()

        response = self.client.get('/api/produtos/codeexists/0/              1', format='json')
        self.assertEqual(response.data, True)


