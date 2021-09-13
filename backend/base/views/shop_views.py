from datetime import timezone

from django.contrib.auth.decorators import login_required
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


@api_view(['POST'])
@login_required
def create_shop(request):
    user = request.user
    data = request.data
    shop = Shop.objects.create(
        name=data['name'],
        owner=user,
        createdAt=timezone.now(),
        description=data['description'],
        category=data['category'],
        image=data['image']
    )
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)

