from django.contrib import admin
from .models import Category, Tag, Event, Plattform

admin.site.register(Event)
admin.site.register(Plattform)
admin.site.register(Category)
admin.site.register(Tag)
