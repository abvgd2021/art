from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=20, help_text = "Enter a name", default="name")
    last_name = models.CharField(max_length=20, help_text = "Enter a lastname", default="lastname")
    birthday = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=20, help_text = "Enter a birthplace", default="place")
    bio = models.TextField(max_length=500, help_text = "Enter a bio", default="bio")
    edu = models.CharField(max_length=100, help_text = "Enter a edu", default="edu")
    
    def __str__(self):
        return self.last_name

class Artwork(models.Model):
    title = models.CharField(max_length=50, help_text = "Enter a name of the artwork", default="title")
    author = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    tuple_medium = (('Краски','Краски'), ('Акварель','Акварель'), ('Скульптура','Скульптура'))
    medium = models.CharField(max_length=10, choices=tuple_medium, blank=True, null=True)
    size = models.CharField(max_length=20, help_text = "Enter a size", default="size")
    creation_day = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Owner(models.Model):
    name = models.CharField(max_length=20, help_text = "Enter a name", default="name")
    tuple_status = (('гос','государственное'), ('мун','муниципальное'), ('част','частное'))
    status = models.CharField(max_length=4, choices=tuple_status, blank=True)
    phone = models.CharField(max_length=10, help_text = "Enter a phone", default="phone")
    address = models.CharField(max_length=50, help_text = "Enter a address", default="address")
    
    def __str__(self):
        return self.name

class Showroom(models.Model):
    name = models.CharField(max_length=50, help_text = "Enter a name", default="name")
    area = models.FloatField(help_text = "Enter a area", default="0")
    phone = models.CharField(max_length=10, help_text = "Enter a phone", default="1234567890")
    address = models.CharField(max_length=50, help_text = "Enter a address", default="address")
    o = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Exhibition(models.Model):
    edate = models.DateField(null=True, blank=True)
    tuple_type = (('Картины','Картины'), ('Пр. искусство','Прикладное искусство'), ('Скульптура','Скульптура'))
    etype = models.CharField(max_length=13, choices=tuple_type, blank=True)
    artworks = models.ManyToManyField(Artwork)
    place = models.ForeignKey(Showroom, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.etype
    