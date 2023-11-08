from django.urls import path

from brags.views.brags.view import view_brags

brag_urlpatterns = [
    path('brags/', view_brags),
]