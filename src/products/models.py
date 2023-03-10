from django.db import models
from django.urls import reverse

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
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        # below code will dynamically work even if we change url path in urls.py
        # 'product-detail' is the name of url
        return reverse('products:product-detail',kwargs={"id":self.id})
        # below code won't work if we change path in url.py
        return f"/product/{self.id}"