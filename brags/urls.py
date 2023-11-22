from django.urls import path

from brags.views.brags.view import view_brags
from brags.views.categories.view import list_categories

brag_urlpatterns = [
    path('api/brags/', view_brags),
    path('api/categories/', list_categories),
]