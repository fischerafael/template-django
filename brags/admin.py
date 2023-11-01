from django.contrib import admin

from brags import models

class BragAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Brag, BragAdmin)