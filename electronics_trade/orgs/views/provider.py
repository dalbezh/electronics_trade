from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from orgs.models import Organization
from orgs.serializers import OrganizationListSerializer, ProviderSerializer, ProviderCreateSerializer


class ProviderListView(ListAPIView):
    """
    Организации являющиеся поставщиками
    """
    queryset = Organization.objects.all().prefetch_related("providers")
    serializer_class = OrganizationListSerializer

    def get_queryset(self):
        providers = self.queryset
        queryset = self.queryset.filter(providers__provider_id__in=providers)
        country = self.request.GET.get('country', None)
        if country:
            return queryset.filter(country__icontains=country)
        else:
            return queryset


class ProviderView(RetrieveUpdateDestroyAPIView):
    """
    Организация являющиеся поставщиком
    """
    queryset = Organization.objects.all().prefetch_related("providers")
    serializer_class = ProviderSerializer

    def get_queryset(self):
        providers = self.queryset
        return self.queryset.filter(providers__provider_id__in=providers)


class ProviderCreateView(CreateAPIView):
    """
    Создание поставщика
    """
    queryset = Organization.objects.all().prefetch_related("providers")
    serializer_class = ProviderCreateSerializer
