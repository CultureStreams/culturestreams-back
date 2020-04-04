from django.contrib import admin
from .models import Category, Event, Plattform, Organizer


class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','start','category','organizer','freeOfCharge','availableLiveOnly','link',)
    ordering = ('id','name','start','category','organizer','freeOfCharge','availableLiveOnly',)
    search_fields = ('name','organizer')
    # def get_tags(self, obj):
    #     return "\n".join([p.name for p in obj.tags.all()])

class PlattformAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','organizer','freeOfCharge','availableLiveOnly','link','description','image',)
    ordering = ('id','name','link',)
    search_fields = ('name','organizer',)
    # def get_tags(self, obj):
    #     return "\n".join([p.name for p in obj.tags.all()])

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','website','description','image','category','datePublished',)
    ordering = ('id','name','slug','website','description','image','category','datePublished',)
    search_fields = ('name','organizer',)
    # def get_tags(self, obj):
    #     return "\n".join([p.name for p in obj.tags.all()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug',)
    ordering = ('id','name','slug',)
    search_fields = ('name',)

# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id','name','slug',)
#     ordering = ('id','name','slug',)
#     search_fields = ('name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Plattform, PlattformAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tag, TagAdmin)
admin.site.register(Organizer, OrganizerAdmin)
