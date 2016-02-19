from django.db import models


class Supplier(models.Model):
    code = models.IntegerField('código', unique=True,
                               error_messages = {  'unique': 'Esse código já está sendo usado por outro fornecedor, tente outro código'})
    company = models.CharField('razão social', max_length=100)
    trade = models.CharField('nome fantasia',max_length=100, blank=True)
    cnpj = models.CharField('cnpj', max_length=14, blank=True)
    observations = models.TextField('observações', blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    class Meta:
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

