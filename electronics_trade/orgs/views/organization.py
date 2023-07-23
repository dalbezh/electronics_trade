from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from orgs.models import Organization
from orgs.serializers import OrganizationListSerializer, OrganizationCreateSerializer, OrganizationSerializer


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


class OrganizationCreateView(CreateAPIView):
    """
    Создание организации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer


class OrganizationView(RetrieveUpdateDestroyAPIView):
    """
    Организация
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

