# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Employee(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)

# Create your models here.
