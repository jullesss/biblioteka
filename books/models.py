from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    pages_number = models.IntegerField()
    pub_year = models.IntegerField()
    pub_by = models.CharField(max_length=200)
    img_url = models.URLField(max_length=250)
    description = models.TextField(null=True)

    users = models.ManyToManyField("users.User", related_name="books")

