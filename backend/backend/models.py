# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djongo import models as dmodels

class User(models.Model):
    _id         = models.BigAutoField(primary_key=True)
    username    = models.CharField(max_length=500)
    firstName   = models.CharField(max_length=500)
    lastName    = models.CharField(max_length=500)
    email       = models.EmailField()

    @property
    def full_name(self):
        return '%s %s' % (self.firstName, self.lastName)

class Photo(models.Model):
    _id         = models.CharField(unique=True, max_length=500, primary_key=True)
    photoName   = models.CharField(max_length=500)
    authorId    = models.ForeignKey('User', on_delete=models.CASCADE)
    author      = models.CharField(max_length=500)
    tags        = dmodels.ArrayModelField(model_container='Tag')
    date        = models.DateField(auto_now=True)
    image       = models.ImageField()

class Tag(models.Model):
    _id        = models.CharField(unique=True, max_length=20, primary_key=True)