from django.contrib import admin

from brags import models

class TagsInline(admin.TabularInline):
    model = models.BragTag
    extra = 1

class BragAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TagsInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Brag, BragAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category, CategoryAdmin)