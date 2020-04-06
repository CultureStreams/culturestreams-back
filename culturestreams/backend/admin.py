from django.contrib import admin
from .models import Category, Event, Plattform, Organizer

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','tagList','start','category','organizer','link','freeOfCharge','availableLiveOnly')
    ordering = ('id','name','start','category','organizer','freeOfCharge','availableLiveOnly',)
    search_fields = ('name','organizer')
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tagList(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

class PlattformAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','tagList','category','organizer','freeOfCharge','availableLiveOnly','link','description','image',)
    ordering = ('id','name','link',)
    search_fields = ('name','organizer',)
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tagList(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','tagList','website','description','image','category','datePublished',)
    ordering = ('id','name','slug','website','description','image','category','datePublished',)
    search_fields = ('name','organizer',)
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tagList(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug',)
    ordering = ('id','name','slug',)
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Plattform, PlattformAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Organizer, OrganizerAdmin)
