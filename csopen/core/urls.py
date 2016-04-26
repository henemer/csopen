from csopen.core.views import CustomerGetMaxCode, CustomerCodeExists, CustomerPostListView, \
    CustomerGetPutDeleteView, SupplierGetMaxCode, SupplierPostListView, SupplierGetPutDeleteView, SupplierCodeExists, \
    ProductPostListView, ProductGetPutDeleteView, ProductCodeExists
from django.conf.urls import url

urlpatterns = [
    url(r'^clientes/getmaxcode/$', CustomerGetMaxCode.getCode),
    url(r'^clientes/codeexists/(?P<id>[0-9]+)/(?P<code>[0-9]+)$', CustomerCodeExists.codeExists),
    url(r'^clientes/$', CustomerPostListView.as_view()),
    url(r'^clientes/(?P<pk>[0-9]+)$', CustomerGetPutDeleteView.as_view()),

    url(r'^fornecedores/getmaxcode/$', SupplierGetMaxCode.getCode),
    url(r'^fornecedores/codeexists/(?P<id>[0-9]+)/(?P<code>[0-9]+)$', SupplierCodeExists.codeExists),
    url(r'^fornecedores/$', SupplierPostListView.as_view()),
    url(r'^fornecedores/(?P<pk>[0-9]+)$', SupplierGetPutDeleteView.as_view()),

    url(r'^produtos/codeexists/(?P<id>[0-9]+)/(?P<code>.*)$', ProductCodeExists.codeExists),
    url(r'^produtos/$', ProductPostListView.as_view()),
    url(r'^produtos/(?P<pk>[0-9]+)$', ProductGetPutDeleteView.as_view()),

]