from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2,max_digits=100)

    def get_absolute_url(self):
        return reverse('article:article-detail', kwargs={"id":self.id})
