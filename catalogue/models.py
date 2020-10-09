# Custom Product models for the project.
from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
# Custom CPU Model

class cpu(models.Model):
    #cpu_Brand = models.CharField()
    cpu_Name = models.CharField(max_length=255)
    cpu_Mark = models.IntegerField()
    cpu_Rank = models.IntegerField()
    cpu_Value = models.IntegerField()
    cpu_Price = models.IntegerField()

'''
# Create your models here.
class item_Category(models.Model):

    class ItemNames(models.TextChoices):
        PROCESSOR = 'Processor'
        GRAPHICS_CARD = 'Graphics Card'
        RAM = 'RAM'
        MOTHERBOARD = 'Motherboard'
        STORAGE = 'Storage'
        POWER_SUPPLY = 'Power Supply'

    item_CategoryName = models.CharField(max_length = 14, choices = ItemNames.choices, default= ItemNames.PROCESSOR)

class Item(models.Model):
    item_UniqueCode = models.CharField(max_length=30)
    item_Name = models.CharField(max_length=30)
    item_Category = models.ForeignKey(item_Category, on_delete=models.CASCADE)
    item_Description = models.TextField()

    class ItemConditionName(models.TextChoices):
        NEW = 'New'
        BNIB = 'Brand New in Box'
        USED = 'Old'
        MOTHERBOARD = 'Motherboard'

    item_Condition = models.CharField(max_length = 30, choices = ItemConditionName.choices, default= ItemConditionName.BNIB)
    item_CrawlerRowNumber = models.IntegerField()
'''
# Put as last line
from oscar.apps.catalogue.models import *
