from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Count
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer


def getSortedCategories():
    return Category.objects.annotate( count= Count( 'post' ) ).order_by( '-count' )

def category_detail( request, slug ):
    category = get_object_or_404( Category, slug= slug )

    context = {
        'category': category,
        'posts': category.post_set.all()
    }

    return render( request,'blog/category_detail.html', context )

#def post_list(request):#
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#

    #return render(request, 'blog/post_list.html', {'posts': posts, 'categories': getSortedCategories()})#

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


    def get(self, request, format=None):
         posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
         serializer = PostSerializer(posts, many=True)
         return Response(serializer.data)

    @permission_classes((IsAdminUser, ))
    def post(self, request, format=None):
        user = request.user
        serializer = PostSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#def post_detail(request, slug, pk):#
    #post = get_object_or_404(Post, pk=pk)#
    #return render(request, 'blog/post_detail.html', {'post': post})#

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
