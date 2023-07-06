from django.db import models


class book_state(models.TextChoices):
    GOOD = "good"
    MEDIUM = "medium"
    BAD = "bad"


class Copy(models.Model):
    class Meta:
        ordering = ("id",)
    available = models.BooleanField(default=True)
    state = models.CharField(
        max_length=20,
        choices=book_state.choices,
        default=book_state.GOOD
        )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_copies",
    )
    loans = models.ManyToManyField(
        "copies.Copy",
        through="loans.Loan",
        related_name="loan_copies"
    )
