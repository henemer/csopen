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


class Customer(models.Model):
    code = models.IntegerField('código', unique=True,
                               error_messages= {'unique': 'Este código já está sendo usado por outro cliente, tente outro código'})
    name = models.CharField('nome', max_length=50)
    nickname = models.CharField('nickname', max_length=50, blank=True)
    address = models.CharField('endereço', max_length=40, blank=True)
    number = models.CharField('número', max_length=10, blank=True)
    district = models.CharField('bairro', max_length=30, blank=True)
    city = models.CharField('cidade', max_length=30, blank=True)
    state = models.CharField('estado', max_length=2, blank=True)
    zipcode = models.CharField('cep', max_length=10, blank=True)
    cpf = models.CharField('cpf', max_length=18, blank=True)
    rg = models.CharField('rg', max_length=20, blank=True)
    phone1 = models.CharField('telefone1', max_length=16, blank=True)
    phone2 = models.CharField('telefone2', max_length=16, blank=True)
    phone3 = models.CharField('telefone3', max_length=16, blank=True)
    contact = models.CharField('contato', max_length=30, blank=True)
    email = models.EmailField('email',max_length=80, blank=True)
    complement = models.CharField('complemento',max_length=30, blank=True)
    observations = models.TextField('observações', blank=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Product(models.Model):
    code = models.CharField('código', max_length=15, unique=True,
                               error_messages = {  'unique': 'Esse código já está sendo usado por outro produto, tente outro código'})
    description = models.CharField('descrição', max_length=50)
    unity = models.CharField('unidade',max_length=3, blank=True)
    cost_price = models.DecimalField('preço de custo', max_digits=18, decimal_places=4, default=0)
    profit_margin = models.DecimalField('margem de lucro', max_digits=7, decimal_places=4, default=0)
    price = models.DecimalField('preço de venda', max_digits=18, decimal_places=2, default=0)
    amount = models.DecimalField('quantidade', max_digits=18, decimal_places=3, default=0)
    reference = models.CharField('referência', max_length=20, blank=True)
    max_stock = models.DecimalField('estoque máximo', max_digits=18, decimal_places=3, default=0)
    min_stock = models.DecimalField('estoque mínimo', max_digits=18, decimal_places=3, default=0)
    bar_code = models.CharField('codigo de barras', max_length=14, blank=True)
    ncm = models.CharField('NCM', max_length=8, blank=True)
    observations = models.TextField('observaçẽos', blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

