from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Shop
from ..serializers import ShopSerializer


@api_view(["GET"])
def get_shops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_shop(request, pk):
    shop = Shop.objects.get(_id=pk)
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def create_shop(request):
    user = request.user
    data = request.data
    shop = Shop.objects.create(
        name='Sample Name',
        owner=user,
        createdAt=datetime.now(),
        description=' ',
        category='Sample Category',
    )
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_shop(request, pk):
    data = request.data
    user = request.user
    shop = Shop.objects.get(_id=pk)
    shop.name = data['name']
    shop.owner = user
    shop.description = data['description']
    shop.category = data['category']

    shop.save()

    serializer = ShopSerializer(shop, many= False)
    return Response(serializer.data)

