from django.db import models


class book_Estate(models.TextChoices):
    good = "good"
    medium = "medium"
    bad = "bad"


class Copy(models.Model):
    class Meta:
        ordering = ("id",)
    available = models.BooleanField(null=False)
    estate = models.CharField(
        choices=book_Estate.choices,
        default=book_Estate.good
        )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book",
    )
