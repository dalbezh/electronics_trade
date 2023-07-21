from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата выхода продукта")

    def __str__(self):
        return '%s: %s' % (self.name, self.model)


class Organization(models.Model):

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    class OrganizationForm(models.IntegerChoices):
        FACTORY = 0, _("Завод")
        RETAIL = 1, _("Розничная сеть")
        SOLE_TRADER = 2, _("Индивидуальный предприниматель")

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
    products = models.ManyToManyField(Product, verbose_name="Продукты")

    def __str__(self):
        return '%s' % self.name


class ProviderOrganization(models.Model):

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    provider = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="providers",
        verbose_name="Поставщик"
    )
    seller = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="debt_to",
        verbose_name="Заказчик",
        null=True,
        blank=True
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Задолженность",
        null=True,
        blank=True
    )

    def __str__(self):
        return '%s' % self.provider
