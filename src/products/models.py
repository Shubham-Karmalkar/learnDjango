from django.db import models


"""
whenever we make change in models.py we need to run below two commands
1. python manage.py makemigrations
2. python manage.py migrate
this will sync our database tables according to models if any changes are made
as we know this is ORM mean our table are getting created with models and we
don't need to create those manually
"""

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(null=True,blank=True) #here null has to do with DB and blank has to do with UI
    featured = models.BooleanField()