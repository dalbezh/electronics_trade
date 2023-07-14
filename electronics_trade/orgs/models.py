from django.db import models


class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата выхода продукта")


class Organization(models.Model):

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    class OrganizationForm(models.IntegerChoices):
        factory = 0, "Фабрика"
        retail = 1, "Редактор"
        sole_trader = 2, "Индивидуальный предприниматель"

    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(blank=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    building = models.CharField(max_length=10, verbose_name="Номер дома")
    organization_form = models.PositiveSmallIntegerField(
        choices=OrganizationForm.choices,
        verbose_name="Форма организации"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    products = models.ManyToManyField(Product)


class ProviderOrganization(models.Model):

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    provider = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="providers")
    seller = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="sellers")
    debt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Задолженность")
