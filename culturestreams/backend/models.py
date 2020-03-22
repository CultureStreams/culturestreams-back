from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField('Name', max_length=200)
    #category_description = models.CharField(max_length=200)
    #category_icon =
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Name', max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Titel', max_length=200)
    organizer = models.CharField('Organisator', max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    availableLiveOnly = models.BooleanField(default=True)
    #reccuring = models.BooleanField(default=False)
    link = models.URLField('Link', max_length=250)
    description = models.CharField('Beschreibung', max_length=400)
    image = models.URLField('Bild', blank=True, max_length=250)
    #event_contact =
    #event_location =
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    #event_cost =
    datePublished = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.title

class Plattform(models.Model):
    title = models.CharField('Titel', max_length=200)
    provider = models.CharField('Anbieter', max_length=200)
    freeOfCharge = models.BooleanField(default=True)
    availableLiveOnly = models.BooleanField(default=True)
    link = models.URLField('Link', max_length=250)
    description = models.CharField('Beschreibung', max_length=400)
    image = models.URLField('Bild', blank=True, max_length=250)
    #event_contact =
    #event_location =
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    #event_cost =
    def __str__(self):
        return self.title + ' by ' + self.provider
