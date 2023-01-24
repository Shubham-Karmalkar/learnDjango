
from django.urls import path
from .views import (
    product_detail_view,
    product_create_view, 
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
    )
"""
So basically the naming of the urls is done for the purpose of 
1. reverse from django.urls which will help to get absolute path
2. help in dynamic routing i.e even if we change url path in urls.py
    we don't have to do code changes on all the places where we used it
    as we now will be serching urls with name instead of path
"""
"""
we have to add name space as belows and add that name space in model
where we are getting url path with name
and reason for adding this is sometimes what happens if we have multiple 
urls in same place i.e in urls.py of the project(and not of app)
with the same name (i.e name=<some_name>) then dynamically routing that 
we place in model does not work properly
1. so first we seperate urls of same type from project's urls.py 
    and will add in url.py of app
2. then we will give name space to it
3. then we will add that name space in model
4. then it will not cause any issue
"""
app_name = 'products'
urlpatterns = [
    path('',product_list_view, name='product-list'),
    path('<int:id>/',dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete',product_delete_view),
]
