from csopen.core.models import Supplier, Customer
from csopen.core.serializers import SupplierSerializer, CustomerSerializer
from django.db.models import Max
from django.shortcuts import render
from rest_framework import status, generics, filters, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


def home(request):
    return render(request, 'index.html')


class CustomerGetPutDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response('Ok', status=status.HTTP_200_OK)

class CustomerPostListView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filter_fields =   {'code': ['exact'],
                       'name': ['icontains'],
                       'nickname': ['icontains'],
                      }


class CustomerGetMaxCode(ModelViewSet):
    @api_view(['GET'])
    def getCode(request):
        code = Customer.objects.all().aggregate(Max('code'))
        if code['code__max'] == None:
            maxCode = 1
        else:
            maxCode = code['code__max'] + 1
        return Response(maxCode)


class CustomerCodeExists():
    @api_view(['GET'])
    def codeExists(request, id, code):
        result =  Customer.objects.exclude(id=id).filter(code=code)
        if not result:
            return Response(False)

        return Response(True)



class SupplierGetPutDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response('Ok', status=status.HTTP_200_OK)

class SupplierPostListView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filter_fields =   {'code': ['exact'],
                       'company': ['icontains'],
                       'trade': ['icontains'],
                      }


class SupplierGetMaxCode(ModelViewSet):
    @api_view(['GET'])
    def getCode(request):
        code = Supplier.objects.all().aggregate(Max('code'))
        if code['code__max'] == None:
            maxCode = 1
        else:
            maxCode = code['code__max'] + 1
        return Response(maxCode)


class SupplierCodeExists():
    @api_view(['GET'])
    def codeExists(request, id, code):
        result =  Supplier.objects.exclude(id=id).filter(code=code)
        if not result:
            return Response(False)

        return Response(True)
