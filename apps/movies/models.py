from django.db import models
from cloudinary.models import CloudinaryField
from apps.category.models import Category


# Create your models here.
class Movies(models.Model):
    MY_CHOICES = (("Newly Released", "Newly Released"), ("Upcoming", "Upcoming"))

    class Meta(object):
        db_table = "Movie"
    name = models.CharField('Name', blank=False, null = False, max_length = 30 )
    
    description = models.TextField('description', blank=True, null=True, max_length=500)

    image = CloudinaryField("image", blank=True, null=True)

    trailer_link = models.CharField('trailer', blank=False, null = False, max_length = 300 )

    rating = models.FloatField('rating', blank=True, null=True)

    movie_duration = models.IntegerField(
        'duration', blank=False, null=False, default=45
    )
    state = models.CharField(
        'state', blank=False, null=False, max_length=50, default='USA'
    )
    release_type = models.CharField(
        'release_type', blank=False, null=False, max_length=50, choices=MY_CHOICES
    )
    release_date = models.IntegerField(
        'release date', blank=False, null=False
    )

    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE,  default=1
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
    def __str__(self):
        return self.name