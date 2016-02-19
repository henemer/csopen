from csopen.core.views import SupplierView
from django.conf.urls import url

urlpatterns ={
    url(r'^fornecedores/$', SupplierView.supplier_list),
    url(r'^fornecedores/(?P<pk>[0-9]+)$', SupplierView.supplier_detail),
}