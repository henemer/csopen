from csopen.core.models import Supplier, Customer
from csopen.core.serializers import SupplierSerializer, CustomerSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


def home(request):
    return render(request, 'index.html')

class SupplierView:
    @api_view(['GET', 'POST'])
    def supplier_list(request, format=None):
        if request.method== 'GET':
            suppliers = Supplier.objects.all()
            serializer = SupplierSerializer(suppliers, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            supplier = SupplierSerializer(data=request.data)
            if supplier.is_valid():
                supplier.save()
                return Response(supplier.data, status=status.HTTP_201_CREATED)
            return Response(supplier.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def supplier_detail(request, pk, format=None):
        """
        Retrieve, update or delete a supplier instance.
        """
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SupplierSerializer(supplier)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = SupplierSerializer(supplier, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            supplier.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerView:
    @api_view(['GET', 'POST'])
    @parser_classes((JSONParser,))
    def customer_list(request, format=None):
        if request.method== 'GET':
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
         #   return Response({'received data': request.data})
            customer = CustomerSerializer(data=request.data)
            if customer.is_valid():
                customer.save()
                return Response(customer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(customer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def customer_detail(request, pk, format=None):
        """
        Retrieve, update or delete a customer instance.
        """
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            customer.delete()
            return Response({'ok'}, status=status.HTTP_200_OK)