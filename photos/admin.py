from django.contrib import admin
from django.utils.safestring import mark_safe

from photos.models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('image_tag',)

    fieldsets = (
        ("Name and description", {
            'fields': ('name', 'description',),
            'classes': ('wide',)

        }),
        ('URL', {
            'fields': ('url', 'image_tag',),
            'classes': ('wide',)

        }),
    )


    def image_tag(self, photo):
        return mark_safe("<img src={0} width=400>".format(photo.url))

admin.site.register(Photo, PhotoAdmin)