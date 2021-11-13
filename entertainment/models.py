from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Catigorie(models.Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Cast(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Common(models.Model):
    title = models.CharField(max_length=255)
    plot = models.TextField(null=True)
    relased = models.DateField(null=True)
    catigories = models.ManyToManyField('Catigorie')
    casts = models.ManyToManyField('Cast')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Movie(Common):
    poster = models.ImageField(null=True, blank=True, upload_to='entertainment/movies/images')
    run_time = models.IntegerField(null=True)
    class Meta:
        ordering = ['-relased']

class Series(Common):

    poster = models.ImageField(null=True, blank=True, upload_to='entertainment/series/images')
    


    class Meta:
        ordering = ['-relased']
        verbose_name_plural = 'Serieses'


class Seisson(Common):

    series = models.ForeignKey('Series', related_name='series_title',on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Seissons'

class Eposides(Common):
    runtime = models.IntegerField()
    seisson = models.ForeignKey('Seisson', related_name='seisson_title',on_delete=CASCADE)
    

    class Meta:
        verbose_name_plural = 'Eposides'


