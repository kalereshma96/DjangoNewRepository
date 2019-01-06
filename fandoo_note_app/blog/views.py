from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'xyz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 2, 2019'
    },
    {
        'author': 'abc',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 2, 2019'
    }
]


def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# from django.shortcuts import render
# from .models import Post
#
#
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)
#
#
# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})