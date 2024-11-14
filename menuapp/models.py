from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from restaurants.models import Restaurant


class MenuCategory(MPTTModel):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_categories",
                                   verbose_name="რესტორნები")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='მშობელი')
    cover_image = models.ImageField(upload_to="category_covers/", blank=True, null=True, verbose_name="კატეგორიის ფოტო")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name="სახელი")
    photo = models.ImageField(upload_to="dish_photos/", blank=True, null=True, verbose_name="ფოტო")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="ფასი")
    category = TreeForeignKey(MenuCategory, on_delete=models.CASCADE, related_name="dishes", verbose_name="კატეგორია")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('გ', 'გრამი'),
        ('მლ', 'მილილიტრი'),
        ('ც', 'ცალი'),
    ]
    name = models.CharField(max_length=255, verbose_name="სახელი")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="ingredients", verbose_name="სახელი")
    quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,verbose_name="რაოდენობა")
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, blank=True, verbose_name="ერთეული")
    description = models.TextField(blank=True, verbose_name="აღწერა")
    image = models.ImageField(upload_to='ingredients/', blank=True, verbose_name="ფოტო")

    def __str__(self):
        return self.name

