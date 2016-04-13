from csopen.core.views import SupplierView, CustomerView
from django.conf.urls import url

urlpatterns ={
    url(r'^fornecedores/$', SupplierView.supplier_list),
    url(r'^fornecedores/(?P<pk>[0-9]+)$', SupplierView.supplier_detail),
    url(r'^clientes/$', CustomerView.customer_list),
    url(r'^clientes/(?P<pk>[0-9]+)$', CustomerView.customer_detail),

}