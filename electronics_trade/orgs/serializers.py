from django.db import transaction
from rest_framework import serializers

from orgs.models import Organization, Product, ProviderOrganization


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продукта.
    """
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ("id", )


class DebtToSerializer(serializers.ModelSerializer):
    """
    Сериализатор о поставщике для заказчика.
    Нужен, для того чтобы отдавать поле debt_to,
    содержащий информацию о сумме задолжности и организации которой должны.
    """
    provider = serializers.SlugRelatedField(queryset=Organization.objects.all(), slug_field="name")
    debt = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)

    class Meta:
        model = ProviderOrganization
        fields = ('provider', 'debt')


class OrganizationListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для всех организация.
    Для того чтобы список не был громоздким сделано поле products_count
    """
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


class OrganizationCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания организаций
    """
    email = serializers.EmailField()
    debt_to = DebtToSerializer(many=True, required=False)
    organization_form = serializers.ChoiceField(
        required=True,
        choices=Organization.OrganizationForm
    )

    def create(self, validated_data):
        products = validated_data.pop('products', [])
        instance = Organization.objects.create(**validated_data)
        for product in products:
            instance.products.add(product)
        return instance

    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'street', 'building', \
                  'products', 'organization_form', 'debt_to', 'created')
        read_only_fields = ("id", "created")


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для организации
    """
    email = serializers.EmailField()
    debt_to = DebtToSerializer(many=True, required=False)
    organization_form = serializers.ChoiceField(
        required=True,
        choices=Organization.OrganizationForm
    )

    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'street', 'building', \
                  'products', 'organization_form', 'debt_to', 'created')
        read_only_fields = ("id", "created")


class ProviderSerializer(OrganizationSerializer):
    """
    Сериализатор для организаций поставщиков
    """
    organization_form = serializers.ChoiceField(
        required=True,
        choices=Organization.OrganizationForm
    )

    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'street', 'building', \
                  'products', 'organization_form', 'created')
        read_only_fields = ("id", "created")


class ProviderCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания организаций поставщиков
    """
    def create(self, validated_data):
        products = validated_data.pop('products', [])
        with transaction.atomic():
            instance = Organization.objects.create(**validated_data)
            ProviderOrganization.objects.create_or_update(provider_id=instance.id)
            for product in products:
                instance.products.add(product)
        return instance

    class Meta:
        model = Organization
        fields = ('id', 'email', 'name', 'country', 'city', 'street', 'building', \
                  'products', 'organization_form', 'created')
        read_only_fields = ("id", "created")
