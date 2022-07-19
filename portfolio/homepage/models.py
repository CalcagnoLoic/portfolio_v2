from django.db import models
from PIL import Image


class AddProjects(models.Model):
    image = models.ImageField()
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    langage1 = models.ImageField(null=True)
    langage2 = models.ImageField(null=True)
    langage3 = models.ImageField(null=True, blank=True)
    langage4 = models.ImageField(null=True, blank=True)
    repository = models.CharField(max_length=200)
    link_projet = models.CharField(max_length=200)
