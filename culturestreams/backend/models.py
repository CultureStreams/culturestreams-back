from django.db import models
from autoslug import AutoSlugField
from .helpers import CustomDateTimeField
import datetime

class Tag(models.Model):
    name = models.CharField('Name', max_length=200)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    icon = models.URLField('Icon-Link', null=True, blank=True, max_length=250)
    #description TODO ?
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    #description TODO ?
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'subcategories'
    def __str__(self):
        return self.parent.name + ' --> ' + self.name

class Organizer(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    website = models.URLField('Webseite', null=True, blank=True, max_length=250)
    description = models.CharField('Beschreibung', null=True, blank=True, max_length=400)
    image = models.URLField('Bild', null=True, blank=True, max_length=250)
    #eventContact TODO
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    datePublished = CustomDateTimeField(auto_now_add=True)
    #lastUpdated TODO = CustomDateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Titel', max_length=200)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    freeOfCharge = models.BooleanField(default=True)
    #eventCost abhängig von freeOfCharge=False TODO
    availableLiveOnly = models.BooleanField(default=True)
    #reccuring TODO
    #reccuring details TODO
    link = models.URLField('Link', max_length=250)
    description = models.CharField('Beschreibung', max_length=400)
    image = models.URLField('Bild', blank=True, max_length=250)
    #eventContact TODO
    #eventLocation TODO
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    datePublished = models.DateTimeField(auto_now_add=True)
    #lastUpdated TODO = CustomDateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Plattform(models.Model):
    name = models.CharField('Titel', max_length=200)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True, blank=True)
    freeOfCharge = models.BooleanField(default=True)
    availableLiveOnly = models.BooleanField(default=True)
    link = models.URLField('Link', max_length=250)
    description = models.CharField('Beschreibung', max_length=400)
    image = models.URLField('Bild', blank=True, max_length=250)
    #eventContact TODO
    #eventLocation TODO
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name + ' by ' + self.organizer.name
