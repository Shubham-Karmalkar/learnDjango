from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request,*args,**kwargs):
    my_context = {
        "my_text": "This is Text",
        "my_num": 1234586,
        "my_list":["shkubha","naruto","hinata",312]
    }
    return render(request, "contact.html", my_context)