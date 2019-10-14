from django.db import models

class User(models.Model):
    _id         = models.BigIntegerField().unique()
    username    = models.CharField()
    firstName   = models.CharField()
    lastName    = models.CharField()
    email       = models.CharField()

    @property
    def full_name(self):
        return '%s %s' % (self.firstName, self.lastName)

class Photo(models.Model):
    _id         = models.CharField().unique()
    photoName   = models.CharField()
    authorId    = models.CharField()
    author      = models.CharField()
    tags        = models.CharField()
    date        = models.DateField().auto_now()
    image       = models.ImageField()
