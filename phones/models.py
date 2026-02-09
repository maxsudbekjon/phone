from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    battery = models.IntegerField(null=True, blank=True)
    cycles = models.IntegerField(null=True, blank=True)
    issues = models.JSONField(default=list, null=True, blank=True)
    verified = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model}"


class PhoneVariant(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='variants')
    ram = models.CharField(max_length=20)
    storage = models.CharField(max_length=20)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()

    class Meta:
        unique_together = ('phone', 'ram', 'storage', 'color')

    def __str__(self):
        color = self.color.name if self.color else 'No color'
        return f"{self.phone} {self.ram}/{self.storage} {color}"


class Image(models.Model):
    image = models.ImageField(upload_to='phone')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.phone}"
