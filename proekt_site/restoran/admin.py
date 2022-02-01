from django.contrib import admin
from .models import Bluda, Restoran, Kategor

class BludaAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'kategor', 'full_text',)
    list_filter = ('kategor', )

admin.site.register(Bluda, BludaAdmin)
admin.site.register(Restoran)
admin.site.register(Kategor)

