from django.db import models


class Supplier(models.Model):
    code = models.IntegerField()
    company = models.CharField(max_length=100)
    trade = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    observation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
