from rest_framework.decorators import api_view
from rest_framework.response import Response

from brags.use_cases.list_brags import ListBrags
from brags.views.brags.serializers import ListBragsSerializer

@api_view(['GET', 'POST'])
def view_brags(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    
    service = ListBrags()
    output = service.execute(
        user_id=1
    )

    # response = []
    # for brag in output:
    #     formatted_tags = []
    #     for brag_tag in brag.tags:           
    #         formatted_tags.append(brag_tag.tag.title)

    #     formatted = {
    #         'id': brag.id,
    #         'title': brag.title,
    #         'duration': brag.duration,
    #         'category': brag.category.title,
    #         'description': brag.description,
    #         'extra_link': brag.extra_link,
    #         'is_public': brag.is_public,
    #         'status': brag.status,
    #         'tags': formatted_tags
    #     } 
    #     response.append(formatted)

    return Response(ListBragsSerializer(output, many=True).data)