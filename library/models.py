from django.db import models


# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=55)
    isbn = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ["author"]
        index_together = (("isbn"),)
