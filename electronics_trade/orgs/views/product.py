from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from orgs.models import Product
from orgs.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    Представление для продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering = ["name"]