from rest_framework import serializers
from csopen.core.models import Supplier, Customer, Product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id','code', 'company', 'trade', 'cnpj', 'observations')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','code', 'name', 'nickname', 'address', 'number',
                  'district', 'city', 'state', 'zipcode','cpf', 'rg',
                  'phone1','phone2', 'phone3','contact', 'email',
                  'complement', 'observations')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  '__all__'


