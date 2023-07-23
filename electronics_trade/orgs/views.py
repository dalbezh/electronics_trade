from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from orgs.serializers import \
    OrganizationListSerializer, OrganizationSerializer, ProductSerializer, ProviderSerializer
from orgs.models import Organization, Product





