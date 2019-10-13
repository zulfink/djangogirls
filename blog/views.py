from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    dict = {'posts': posts}
    return render(request, 'blog/post_list.html', dict)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    dict = {'post': post}
    return render(request, 'blog/post_details.html', dict)
