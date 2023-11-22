from datetime import date

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.models.category.model import Category
from brags.use_cases.categories_list import ListCategories
from brags.views.brags.serializers import ListBragsSerializer


@api_view(['GET'])
def list_categories(request):    
    use_case = ListCategories()
    categories = use_case.execute(request.user.id)
    return Response(ListCategoriesSerializer(categories, many=True).data)



class ListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'id']