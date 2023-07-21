from django.urls import path
from rest_framework import routers

from orgs.views import OrganizationListView, OrganizationView, ProductListView, ProductView, ProviderViewSet

app_name = 'orgs'

router = routers.SimpleRouter()
router.register('provider', ProviderViewSet)

urlpatterns = [
    path('organization', OrganizationListView.as_view(), name="list_organization"),
    path('organization/<pk>', OrganizationView.as_view(), name="organization"),
    path('product', ProductListView.as_view(), name="list_organization"),
    path('product/<pk>', ProductView.as_view(), name="product")
]

urlpatterns += router.urls
