from rest_framework import serializers

from brags.models.brag.model import Brag


class ListBragsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()    

    class Meta:
        model = Brag
        exclude = ['is_public', 'user']

    def get_tags(self, obj):    
        titles = []
        for brag_tag in obj.tags.all():           
            titles.append(brag_tag.tag.title)   
        return titles
    
    def get_category(self, obj):
        return obj.category.title
