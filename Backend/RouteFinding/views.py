from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def route_finding(request, src, dest):
    ans = get_route_cost(src, dest)
    return Response(
        {"path": ans[0], "cost": ans[1]},
        status=status.HTTP_200_OK
    )