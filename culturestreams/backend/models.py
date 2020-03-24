from django.db import models
import datetime
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    #description TODO ?
    #category_icon TODO
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        if k is not None:
            full_path.append(k.name)
        return ' -> '.join(full_path[::-1])
        #return self.name

class Tag(models.Model):
    name = models.CharField('Name', max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Titel', max_length=200)
    organizer = models.CharField('Organisator', max_length=200)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

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
    #eventContact TODO
    #eventLocation TODO
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.title + ' by ' + self.provider
