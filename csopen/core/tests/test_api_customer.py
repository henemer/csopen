from csopen.core.models import Customer
from django.test import TestCase
from django_extensions.db.fields import json
from rest_framework.test import APIClient


class CustomerModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.obj = Customer(
            code=1,
            name='Emerson Henning',
            nickname='Henemer',
            address='Av. República Argentina',
            number='1111',
            complement='Apto.XXX',
            district='Portão',
            city='Curitiba',
            state='PR',
            zipcode='80610260',
            cpf='00000000000',
            rg='555555555-44',
            phone1='41-9999-9999',
            phone2='41-9999-9999',
            phone3='41-9999-9999',
            contact='Emerson',
            email='emerson@henning.com.br',
            observations='Nennhuma observação a fazer')

    def test_post_customer(self):
        j = json.dumps({'code':1, 'name':'Emerson Henning'})
        response = self.client.post('/api/clientes/',
                        content_type='application/json',
                        data = j)
        self.assertEqual(response.status_code, 201)


    def test_retrieve_customer(self):
        self.obj.save()

        response = self.client.get('/api/clientes/1' )

        self.assertContains(response, 'Emerson Henning')


    def test_update_customer(self):
        self.obj.save()

        j = json.dumps({'id':1, 'code':22, 'name':'João da Silva Sauro'})
        response = self.client.put('/api/clientes/1',
                        content_type='application/json',
                        data = j)

        self.assertContains(response, 'João da Silva Sauro')


    def test_delete_customer(self):
        self.obj.save()

        response = self.client.delete('/api/clientes/1')
        self.assertContains(response, 'Ok')


    def test_get_customer(self):
        self.obj.save()

        response = self.client.get('/api/clientes/')

        self.assertContains(response, 'Emerson Henning')


    def test_customer_code_exists(self):
        self.obj.save();

        client = APIClient()
        response = client.get('/api/clientes/codeexists/0/1', format='json')
        self.assertEqual(response.data, True)


    def test_customer_next_code(self):
        self.obj.save()
        client = APIClient()

        response = client.get('/api/clientes/getmaxcode/', format='json')

        self.assertEqual(2, response.data)