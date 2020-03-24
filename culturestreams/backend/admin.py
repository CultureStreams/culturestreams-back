from django.contrib import admin
from .models import Category, Tag, Event, Plattform, Organizer, SubCategory

admin.site.register(Event)
admin.site.register(Plattform)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Organizer)
