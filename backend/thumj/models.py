from django.db import models
# from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

# class Player(models.Model):
#     name = models.CharField(max_length=50)

class Test(models.Model):
    contents = models.CharField(max_length=200)

class Paipu(models.Model):
    # players = models.JSONField()
    ref = models.CharField(max_length=200)
    log = models.JSONField()
    ratingc = models.CharField(max_length=100)
    rule = models.JSONField()
    lobby = models.IntegerField()
    dan = models.JSONField()
    rate = models.JSONField()
    sx = models.JSONField()
    name = models.JSONField()
    title = models.JSONField()