from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all
    template = loader.get_template('index.html')
    context = {
     'posts': posts,
    }
    return HttpResponse(template.render(context,request))

def details(request, post_id):
  post = get_object_or_404(Post, pk = post_id)
  return render(request, 'details.html', {'post' : post})
