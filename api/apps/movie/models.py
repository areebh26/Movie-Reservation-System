from django.db import models


class Movie(models.Model):

    class Genre(models.TextChoices):
        ACTION = "ACTION", "Action"
        COMEDY = "COMEDY", "Comedy"
        DRAMA = "DRAMA", "Drama"
        HORROR = "HORROR", "Horror"
        ROMANCE = "ROMANCE", "Romance"
        THRILLER = "THRILLER", "Thriller"
        SCI_FI = "SCI_FI", "Science Fiction"
        ANIMATION = "ANIMATION", "Animation"

    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    release_date = models.DateField()

    genre = models.CharField(
        max_length=20,
        choices=Genre.choices,
    )

    poster = models.ImageField(
        upload_to="movie_posters/",
        null=True,
        blank=True,
    )

    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)