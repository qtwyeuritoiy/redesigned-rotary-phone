"""
Custom models for the project.
"""

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class CPUProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    socket_type = models.CharField(max_length = 50) #LGA 1151, AM4, TR4
    clock_speed = models.IntegerField() #Measured in MHz
    core_count = models.IntegerField()
    tdp_rating = models.IntegerField() #Measured in W
    cache_capacity = models.IntegerField() #Measured in KB

class MotherboardProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    form_factor = models.CharField(max_length = 50) #ATX, Micro ATX, Mini ITX
    socket_type = models.CharField(max_length = 50) #LGA 1151, AM4, TR4
    chipset_type = models.CharField(max_length = 50) #AMD B450, AMD X470, Intel Z370, Intel B460

class GPUProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    core_count = models.CharField(max_length = 50)
    clock_speed = models.IntegerField() #Measured in MHz
    tdp_rating = models.IntegerField()  #Measured in W
    ram_capacity = models.IntegerField() #Measured in MB

class RAMProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    socket_type = models.CharField(max_length = 50) #DDR4, DDR3
    capacity = models.IntegerField() #Measured in MB
    clock_speed = models.IntegerField() #Measured in MHz
    clock_timing = models.CharField(max_length = 50)

class SSDProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    form_factor = models.CharField(max_length = 50) #2.5", M.2 2280, USB
    interface_type = models.CharField(max_length = 50) #SATA 3, NVMe
    capacity = models.IntegerField() #Measured in GB
    flash_type = models.CharField(max_length = 50) #MLC, TLC, QLC

class HDDProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    form_factor = models.CharField(max_length = 50) #2.5", 3.5", USB
    interface_type = models.CharField(max_length = 50) #SATA 2, SATA 3
    capacity = models.IntegerField() #Measured in GB
    rpm = models.IntegerField()
    cache = models.IntegerField() #Measured in MB

class PowerSupplyProduct(AbstractProduct):
    model_name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    form_factor = models.CharField(max_length = 50) #ATX, SFX, ATX12V
    max_power_out = models.IntegerField() #Measured in W
    efficiency = models.CharField(max_length = 50) #80 PLUS Bronze, 80 PLUS Gold
    modularity = models.CharField(max_length = 50) #Non-modular, Semi-modular, Full-modular


from oscar.apps.catalogue.models import *  # noqa isort:skip
