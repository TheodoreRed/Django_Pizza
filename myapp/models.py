from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    would_return = models.BooleanField()
    comment = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
