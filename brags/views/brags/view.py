from datetime import date

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.use_cases import bag_create, brag_list
from brags.views.brags.serializers import ListBragsSerializer


@api_view(['GET', 'POST'])
def view_brags(request):
    if request.method == 'POST':
        try:
            service = bag_create.CreateBrag()       
            serializer = CreateBragSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            output = service.execute(
                category_id=serializer.validated_data['category_id'],
                duration=serializer.validated_data['duration'],
                title=serializer.validated_data['title'],
                user_id=serializer.validated_data['user_id']
            )
            return Response("Ok")
        except:
            return Response('Error', status=400)
    
    today = date.today()
    service = brag_list.ListBrags()
    output = service.execute(
        user_id=request.user.id,
        day=today
    )
    return Response(ListBragsSerializer(output, many=True).data)

class CreateBragSerializer(serializers.Serializer):
    duration = serializers.DecimalField(max_digits=3, decimal_places=2)
    title = serializers.CharField(max_length=30)
    user_id = serializers.IntegerField()
    category_id = serializers.IntegerField()