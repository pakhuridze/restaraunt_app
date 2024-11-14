from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="restaurants")
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    cover_photo = models.ImageField(upload_to="restaurant_covers/", blank=True, null=True)

    def __str__(self):
        return self.name
