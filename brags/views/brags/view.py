from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.use_cases.list_brags import ListBrags

@api_view(['GET', 'POST'])
def view_brags(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    
    service = ListBrags()
    service.execute(
        user_id=1
    )
    return Response({"message": "Hello, world!"})