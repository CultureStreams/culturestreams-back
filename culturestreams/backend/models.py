from django.db import models
from autoslug import AutoSlugField
from .helpers import CustomDateTimeField
import datetime
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', unique_with=('name'), null=True, blank=True)
    icon = models.URLField('Icon-Link', null=True, blank=True, max_length=250)
    #description TODO ?
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Organizer(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', unique_with=('name'), null=True, blank=True)
    website = models.URLField('Webseite', null=True, blank=True, max_length=250)
    description = models.TextField('Beschreibung', null=True, blank=True, max_length=700)
    image = models.URLField('Bild', null=True, blank=True, max_length=250)
    #eventContact TODO
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)
    datePublished = CustomDateTimeField(auto_now_add=True)
    #lastUpdated TODO = CustomDateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Titel', max_length=200)
    slug = AutoSlugField(populate_from=('name'), unique_with=('name', 'start'), null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    freeOfCharge = models.BooleanField(default=True)
    availableLiveOnly = models.BooleanField(default=True)
    link = models.URLField('Link', max_length=250)
    infoLink = models.URLField('weitere Infos (Link)', null=True, blank=True, max_length=250)
    description = models.TextField('Beschreibung', max_length=1000)
    image = models.URLField('Bild', blank=True, max_length=250)
    #location
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)
    datePublished = models.DateTimeField(auto_now_add=True)
    #lastUpdated TODO = CustomDateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField('Titel', max_length=200)
    slug = AutoSlugField(populate_from='name', unique_with=('name'), null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True, blank=True)
    freeOfCharge = models.BooleanField(default=True)
    availableLiveOnly = models.BooleanField(default=True)
    link = models.URLField('Link', max_length=250)
    description = models.TextField('Beschreibung', max_length=1000)
    image = models.URLField('Bild', blank=True, max_length=250)
    #eventContact TODO
    #eventLocation TODO
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)
    def __str__(self):
        return self.name + ' by ' + self.organizer.name
