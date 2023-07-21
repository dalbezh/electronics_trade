from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from orgs.serializers import OrganizationListSerializer, OrganizationSerializer, ProductSerializer, ProviderSerializer
from orgs.models import Organization, Product


class OrganizationListView(ListAPIView):
    """
    Список организаций
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer
    filter_backends = [OrderingFilter]
    ordering = ["name"]

    def get_queryset(self):
        queryset = self.queryset
        country = self.request.GET.get('country', None)
        if country:
            return queryset.filter(country__icontains=country)
        else:
            return queryset


class OrganizationView(RetrieveUpdateDestroyAPIView):

    queryset = Organization.objects.all().prefetch_related("debt_to")
    serializer_class = OrganizationSerializer


class ProductListView(ListAPIView):
    """
    Список всех продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering = ["name"]


class ProductView(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProviderViewSet(ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = ProviderSerializer

    def get_queryset(self):
        providers = Organization.objects.prefetch_related("providers")
        queryset = self.queryset.filter(providers__id__in=providers)
        country = self.request.GET.get('country', None)
        if country:
            return queryset.filter(country__icontains=country)
        else:
            return queryset
