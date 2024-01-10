from django.db import models
from django.conf import settings

class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название области")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название города")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название района")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name="Город")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, verbose_name="Район")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name="Область")

    def __str__(self):
        return f"{self.region} - {self.city} - {self.district}"

    class Meta:
        verbose_name_plural = "Локации"


class Communication(models.Model):
    name = models.CharField(max_length=100, verbose_name="Коммуникации")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Коммуникации"


class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name="Документы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Документы"


class TargetPurpose(models.Model):
    name = models.CharField(max_length=100, verbose_name="Целовое назначение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Целовое назначение"


class Infrastructure(models.Model):
    name = models.CharField(max_length=100, verbose_name="Инфраструктура")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Инфраструктура"


class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    estate = models.ForeignKey('Estate', on_delete=models.CASCADE, related_name='images', null=True,
                               verbose_name='Объявление')

    def __str__(self):
        return f"{self.estate}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Estate(models.Model):

    CURRENCY_CHOICES = (
        ("1", "USD"),
        ("2", "СОМ"),
        ("3", "Договорная"),
    )

    DEAL_TYPE_CHOICES = (
        ("1", "Продаю участок"),
        ("2", "Продаю дом"),
        ("3", "Продаю под снос"),
        ("4", "Аренда участка"),
        ("5", "Куплю участок/дом"),
    )

    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    # image = models.ImageField(verbose_name="Изображение")
    # images = models.ManyToManyField(Image, related_name='estate_images', null=True, verbose_name="Изображения")
    plot_area = models.PositiveSmallIntegerField(null=True, verbose_name="Площадь участка сот.")
    house_area = models.PositiveSmallIntegerField(null=True, verbose_name="Площадь дома КВ.М")
    deal_type = models.CharField(max_length=30, choices=DEAL_TYPE_CHOICES, default=None, verbose_name="Тип сделки")
    price = models.PositiveIntegerField(null=True, verbose_name="Цена")
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default=None, verbose_name="Валюта")
    phone = models.CharField(max_length=10, verbose_name="Номер телефона")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="Расположение")
    target = models.ForeignKey(TargetPurpose, on_delete=models.SET_NULL, null=True, verbose_name="Целевое назначение")
    communications = models.ManyToManyField(Communication, null=True, verbose_name="Коммуникации")
    documents = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True, verbose_name="Документы")
    infrastructure = models.ManyToManyField(Infrastructure, null=True,
                                       verbose_name="Инфраструктура")

    def __str__(self):
        return f"Объявление: {self.name}"

    class Meta:
        verbose_name_plural = "Объявления"



# class FavoriteItem(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
#     estate = models.ForeignKey(Estate, on_delete=models.CASCADE, verbose_name='Объявление')

