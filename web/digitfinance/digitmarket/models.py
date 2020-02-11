from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=128)
    fullname = models.CharField(max_length=128)
    enname = models.CharField(max_length=128)

class Currency(models.Model):
    name = models.CharField(max_length=32)
    fullname = models.CharField(max_length=32)
    enname = models.CharField(max_length=32)
    symbol = models.CharField(max_length=32)

class Exchange(models.Model):
    name = models.CharField(max_length=128)
    fullname = models.CharField(max_length=128)
    enname = models.CharField(max_length=128)

class Equities(models.Model):
    area = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)
    fullname = models.CharField(max_length=128)
    enname = models.CharField(max_length=128)
    market = models.ForeignKey(Market, on_delete=models.CASCADE) # 市场类型 （主板/中小板/创业板/科创板）
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE) # 交易所
    curr_type = models.ForeignKey(Currency, on_delete=models.CASCADE)
    list_status = models.IntegerField() # 1上市 0退市 2暂停上市
    list_date = models.DateTimeField('date list')
    delist_date = models.DateTimeField('date delist')
    is_hs = models.IntegerField()