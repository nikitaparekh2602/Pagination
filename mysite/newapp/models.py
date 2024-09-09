from django.db import models

class MovieData(models.Model):
    name = models.CharField(max_length=200)
    ratting = models.FloatField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
