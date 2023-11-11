from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.use_cases import brag_list, bag_create
from brags.views.brags.serializers import ListBragsSerializer

@api_view(['GET', 'POST'])
def view_brags(request):
    if request.method == 'POST':
        service = bag_create.CreateBrag()
        output = service.execute(0.10, 'test', 1)
        return Response({"message": "Got some data!", "data": request.data})
    
    service = brag_list.ListBrags()
    output = service.execute(
        user_id=1
    )
    return Response(ListBragsSerializer(output, many=True).data)