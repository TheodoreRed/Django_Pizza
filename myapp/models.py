from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    would_return = models.BooleanField()
    comment = models.TextField()

    def __str__(self):
        return self.name
