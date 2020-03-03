from django.db import models

# Create your models here

class Materials(models.Model):
    house_id = models.IntegerField()
    item_name = models.CharField(max_length=200)
    date_received = models.DateField()
    time_received = models.TimeField()
    quantity = models.IntegerField()
    KILOGRAMS = 'kgs'
    GRAMS = 'g'
    BAGS = 'bags'
    LITERS = 'lt'
    UNIT_CHOICES = [
        (KILOGRAMS, 'Kilograms'),
        (GRAMS, 'Grams'),
        (BAGS, 'Bags'),
        (LITERS, 'Liters'),
    ]
    item_unit = models.CharField(
        max_length=5,
        choices=UNIT_CHOICES,
        default=KILOGRAMS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.house_id)
