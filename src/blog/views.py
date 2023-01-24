from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Blog
from .forms import BlogForm
# Create your views here.

class CourseObjectMixin(object):
    model = Blog
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Blog, id=id)
        return obj

class CourseDeleteView(CourseObjectMixin,View):
    template_name='courses/course_delete.html'

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object']= obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('/blog/')            
        return render(request, self.template_name, context)
    
class CourseUpdateView(CourseObjectMixin,View):
    template_name = 'courses/course_update.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = BlogForm(instance=obj)
            context['form']=form
            context['object']= obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        context = {}
        obj = self.get_object()
        if obj is not None:
            """
            Sending the instance in Form is important 
            otherwise it create new insteance instead of updating
            """
            form = BlogForm(request.POST,instance=obj)
            print(form.is_valid())
            if form.is_valid():
                form.save()
            context['form']=form
            context['object'] = obj
        
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        form = BlogForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = BlogForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Blog.objects.all()
    print(queryset)
    def get(self, request, *args, **kwargs):
        context = {
            'object_list':self.queryset
        }
        return render(request, self.template_name, context)

class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Blog,id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

def my_fbv(request, *args, **kwargs):
    return render(request, 'home.html', {})