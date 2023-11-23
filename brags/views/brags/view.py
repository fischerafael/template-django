from datetime import date

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.use_cases import bag_create, brag_list, brag_delete
from brags.views.brags.serializers import ListBragsSerializer


@api_view(['GET', 'POST', 'DELETE'])
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
        except Exception as e:
            return Response({'error': f'{e}'}, status=400)
    
    if request.method == 'DELETE':
        try:
            service = brag_delete.DeleteBrag()
            serializer = RemoveBragSerializer(data={'brag_id': request.GET['brag_id']})
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            service.execute(
                user_id=request.user.id,
                brag_id=serializer.validated_data['brag_id']
            )            
            return Response('Deleted')
        except Exception as e:
            return Response({'error': f'{e}'}, status=400)

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

class RemoveBragSerializer(serializers.Serializer):
    brag_id = serializers.IntegerField()