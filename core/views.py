from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request=request, template_name="index.html", context={"posts": posts})
