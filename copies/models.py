from django.db import models


class book_state(models.TextChoices):
    good = "good"
    medium = "medium"
    bad = "bad"


class Copy(models.Model):
    class Meta:
        ordering = ("id",)
    available = models.BooleanField(null=False)
    state = models.CharField(
        choices=book_state.choices,
        default=book_state.good
        )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_copies",
    )
    loans = models.ManyToManyField(
        "loans.Loan",
        on_delete=models.CASCADE,
        related_name="loan_copies",
    )
