from rest_framework import serializers
from csopen.core.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('code', 'company', 'trade', 'cnpj', 'observations')





