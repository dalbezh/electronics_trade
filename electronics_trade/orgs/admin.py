from django.contrib import admin

from orgs.models import Product, Organization, ProviderOrganization


class BaseAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    readonly_fields = ("id", )


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ("name", "model", "release_date")


class ProvidersInline(admin.TabularInline):
    model = ProviderOrganization
    readonly_fields = ("provider", "debt")
    show_change_link = True
    fk_name = "seller"
    extra = 0
    max_num = 1
    verbose_name = "Поставщик"
    verbose_name_plural = "Поставщики"


@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    list_display = ("name", "email", "country", "city", "organization_form")
    list_filter = ('city', )

    def get_inlines(self, request, obj):
        if ProviderOrganization.objects.filter(seller_id__exact=obj.id):
            return [ProvidersInline]
        return []


@admin.register(ProviderOrganization)
class ProviderOrganizationAdmin(admin.ModelAdmin):
    list_display = ("provider", "seller", "debt")
    list_display_links = ("provider", )
    list_select_related = True
    search_fields = ("provider", "seller")
    actions = ["flush_debt"]

    @admin.action(description="Отчистить задолженность")
    def flush_debt(self, request, queryset):
        queryset.update(debt=0.0)
