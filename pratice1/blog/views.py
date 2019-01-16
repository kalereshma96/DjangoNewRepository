# In this section different views are created
# like create view, delete view, update view etc.


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    """

    :param request: for all post or fandoo notes
    :return: home page
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """

        :param form: If form is valid create instance
        :return: form
        """
        form.instance.author = self.request.user
        # return super().form_valid(form)

    def test_func(self):
        """

        :return: check request and return true or false
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        """

        :return:
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """

    :param request:
    :return: about.html page
    """
    return render(request, 'blog/about.html', {'title': 'About'})