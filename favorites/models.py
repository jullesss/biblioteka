from django.db import models

class Favorite(models.Model):
    class Meta:
        ordering = ("id",)
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="favorite_book",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="favorite_user",
    )