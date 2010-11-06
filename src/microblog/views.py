from django import http
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from microblog.models import Blog
from microblog.forms import BlogForm

def render_to(template):
    def wrapper(func):
        def wrap(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            if isinstance(result, dict):
                return render_to_response(template,
                      result,
                      context_instance=RequestContext(request))
            else:
                return result
        return wrap
    return wrapper


@render_to('microblog/templates/index.html')
def index(request, form=None):
    return {
        'blogs':Blog.objects.all(),
        'form':form or BlogForm(request.user),
    }

def save_message(request):
    form = BlogForm(request.user, request.POST)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect('/')
    else:
        return index(request, form)
