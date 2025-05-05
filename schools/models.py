from django.db import models

class School(models.Model):
    CATEGORY_CHOICES = [
        ('public', 'Государственная'),
        ('private', 'Частная'),
        ('special', 'Специальная')
    ]

    DISTRICT_CHOICES = [
        ('central', 'Центральный район'),
        ('north', 'Северный район'),
        ('east', 'Восточный район'),
        ('west', 'Западный район')
    ]

    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_info = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='public')
    district = models.CharField(max_length=10, choices=DISTRICT_CHOICES, default='central')
    image = models.ImageField(upload_to='school_images/', blank=True, null=True)
    google_maps_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name