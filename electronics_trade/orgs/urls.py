from django.urls import path
from rest_framework import routers

from orgs.views.product import ProductViewSet
from orgs.views.organization import OrganizationListView, OrganizationCreateView, OrganizationView
from orgs.views.provider import ProviderListView, ProviderCreateView, ProviderView

app_name = 'orgs'

router = routers.SimpleRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('organization', OrganizationListView.as_view(), name="list_organization"),
    path('organization/create', OrganizationCreateView.as_view(), name="create_organization"),
    path('organization/<pk>', OrganizationView.as_view(), name="organization"),
    path('provider', ProviderListView.as_view(), name="list_provider"),
    path('provider/create', ProviderCreateView.as_view(), name="create_provider"),
    path('provider/<pk>', ProviderView.as_view(), name="provider"),
]

urlpatterns += router.urls
