from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
"""
GET is unsecure method than POST in form as 
if given the chance hacker can view and manupulate the 
data in url 
"""
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form":form
#     }
#     return render(request,'products/product_create.html',context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, 'products/product_list_view.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    print(request.method)
    if request.method == 'POST':
        print('deleting the data: ')
        obj.delete()
        return redirect('../')
        
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }

    return render(request, 'products/product_detail.html', context)

def render_initial_data(request):
    initial_data = {
        'title': 'My Initial Title'
    }
    """
        Usually what we do when user want form to update its 
        data we show filled form from the database and give
        it to user to use it
    """
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    print(form.is_valid())
    context = {
        'form':form
    }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm
    
    context = {
        'form':form
    }
    return render(request,'products/product_create.html',context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'description':obj.description
    # }
    # more better approach
    context = {
        'object':obj
    }
    """
    we also need to add this template path in settings.py
    """
    return render(request,"products/product_detail.html", context)