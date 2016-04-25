from django.db import IntegrityError
from django.test import TestCase
from csopen.core.models import Customer
from rest_framework.test import APIRequestFactory, APIClient


class CustomerModelTest(TestCase):
    def setUp(self):
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

    def test_create(self):
        self.obj.save()
        self.assertTrue(Customer.objects.exists())

    def test_customer_code_cannot_repeat(self):
        ''' The code can not be repeated '''
        customer2 = Customer(
          code=1,
          name='XX')

        self.obj.save()
        with self.assertRaises(IntegrityError):
            customer2.save()


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