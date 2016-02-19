from csopen.core.views import SupplierView
from django.conf.urls import url

urlpatterns ={
    url(r'^suppliers/$', SupplierView.supplier_list),
    url(r'^suppliers/(?P<pk>[0-9]+)$', SupplierView.supplier_detail),
}