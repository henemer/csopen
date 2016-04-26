from csopen.core.models import Supplier
from django.test import TestCase
from django_extensions.db.fields import json
from rest_framework.test import APIClient


class SupplierModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.obj = Supplier(
            code=1,
            company='Emerson Henning ME',
            trade='Henning Informática',
            cnpj='00000000000000',
            observations='Alguma observação.'
        )

    def test_post_supplier(self):
        j = json.dumps({'code':1, 'company':'Empresa S.A.'})
        response = self.client.post('/api/fornecedores/',
                        content_type='application/json',
                        data = j)
        self.assertEqual(response.status_code, 201)


    def test_retrieve_supplier(self):
        self.obj.save()

        response = self.client.get('/api/fornecedores/1' )

        self.assertContains(response, 'Emerson Henning ME')


    def test_update_supplier(self):
        self.obj.save()

        j = json.dumps({'id':1, 'code':22, 'company':'Empresa XYZ'})
        response = self.client.put('/api/fornecedores/1',
                        content_type='application/json',
                        data = j)

        self.assertContains(response, 'Empresa XYZ')


    def test_delete_supplier(self):
        self.obj.save()

        response = self.client.delete('/api/fornecedores/1')
        self.assertContains(response, 'Ok')


    def test_get_supplier(self):
        self.obj.save()

        response = self.client.get('/api/fornecedores/')

        self.assertContains(response, 'Emerson Henning ME')


    def test_supplier_code_exists(self):
        self.obj.save();

        client = APIClient()
        response = client.get('/api/fornecedores/codeexists/0/1', format='json')
        self.assertEqual(response.data, True)


    def test_supplier_next_code(self):
        self.obj.save()
        client = APIClient()

        response = client.get('/api/fornecedores/getmaxcode/', format='json')

        self.assertEqual(2, response.data)