from rest_framework import serializers

from brags.models.brag.model import Brag


class ListBragsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Brag
        fields = ['id', 'title', 'duration', 'category', 'description', 'extra_link', 'is_public', 'status', 'tags']

    def get_tags(self, obj):    
        titles = []
        for brag_tag in obj.tags.all():           
            titles.append(brag_tag.tag.title)   
        return titles
