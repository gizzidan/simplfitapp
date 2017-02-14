from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone
from blog.models import Post, Category
from blog.views import getSortedCategories


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'landingpage/base_landing.html', {'posts': posts, 'categories': getSortedCategories()})
# Create your views here.
