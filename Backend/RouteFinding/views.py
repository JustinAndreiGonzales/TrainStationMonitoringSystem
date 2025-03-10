from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Algorithm.routeFinding import get_route_cost

# Create your views here.
@api_view(['GET'])
def route_finding(request, src, dest):
    ans = get_route_cost(src, dest)
    return Response(
        {"path": ans["path"], "cost": ans["cost"]},
        status=status.HTTP_200_OK
    )