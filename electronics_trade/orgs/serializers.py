from rest_framework import serializers

from orgs.models import Organization, Product, ProviderOrganization


class OrganizationListSerializer(serializers.ModelSerializer):

    products_count = serializers.SerializerMethodField()
    organization_form = serializers.ChoiceField(
        required=True,
        choices=Organization.OrganizationForm,
        source='get_organization_form_display'
    )

    class Meta:
        model = Organization
        fields = ('id', 'name', 'country', 'city', 'organization_form', 'products_count')
        read_only_fields = ("id", "created")

    def get_products_count(self, obj):
        return obj.products.count()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProviderOrganizationSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(queryset=Organization.objects.all(), slug_field="name")
    debt = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)

    class Meta:
        model = ProviderOrganization
        fields = ('provider', 'debt')


class OrganizationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    products = ProductSerializer(many=True, read_only=True)
    debt_to = ProviderOrganizationSerializer(many=True, required=False)
    organization_form = serializers.ChoiceField(
        required=True,
        choices=Organization.OrganizationForm,
        source='get_organization_form_display'
    )

    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'products', 'organization_form', 'debt_to', 'created')


class ProviderSerializer(OrganizationSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'products', 'organization_form', 'created')

    def create(self, validated_data):
        provider = Organization.objects.create(**validated_data)
        Organization.objects.providers.set()
        return provider
