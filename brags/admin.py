from django.contrib import admin

from brags.models.brag.model import Brag
from brags.models.brag_tag.model import BragTag
from brags.models.category.model import Category
from brags.models.tag.model import Tag


class TagsInline(admin.TabularInline):
    model = BragTag
    extra = 1
    

class BragAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    inlines = [TagsInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Brag, BragAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)