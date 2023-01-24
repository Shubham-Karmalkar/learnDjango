from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Create your views here.
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
)
"""
Generic view behind the scenes does work with Database
ex. then use form.save() behind the scenes to save data in DB
"""

from .models import Article
from .forms import ArticleModelForm

class ArticleListView(ListView):
    # if we don't have default name we can override by below way
    # template_name= 'article/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article/article_details.html'
    # queryset = Article.objects.all()

    # default serch param is pk to override that use below code
    def get_object(self):
        # self.kwargs has the actual data come with request
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

class ArticleCreateView(CreateView):
    template_name= 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    """
        By default this class ask for path 
        with error stating and asking name of 
        'get_absolute_url'
        and we can override this behaviour and 
        by adding blow code
    """
    """
        method 1
        success_url = '/'
         or 
        method 2
        def get_success_url(self):
            return '/'
    
    """

class ArticleUpdateView(UpdateView):
    template_name= 'article/article_create.html'
    form_class = ArticleModelForm
    # queryset = Article.objects.all()

    def get_object(self):
        # self.kwargs has the actual data come with request
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
    
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name='article/article_delete.html'
    # success_url='../'
    def get_object(self):
        # self.kwargs has the actual data come with request
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
    def get_success_url(self):
        return reverse('article:article-list')
