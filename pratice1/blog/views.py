# In this section different views are created
# like create view, delete view, update view etc.



from django.db import IntegrityError
from django.utils import timezone
import json
from .form import create_note_form, reminder_form
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Notes


class note_list(ListView):
    ''' This is a class based view of django which uses ListView.
	    it returns object_list of objects in database.'''
    model = Notes
    template_name = 'blog/home.html'


def create_note(request):
    try:
        form = create_note_form(request.POST)
        if request.method == "POST":
            print("in post method")
            response_data = {}
            # if form.is_valid():
            instance = form.save(commit=False)
            print("instance = ", instance)
            instance.title = request.POST.get('title')
            print("instance.title = ", instance.title)
            instance.description = request.POST.get('description')
            instance.is_pinned = request.POST.get('is_pinned')
            instance.color = request.POST.get('color')
            # instance.user  = request.POST.get('user')
            instance.save()
            response_data['status'] = True
            response_data['message'] = 'Successfully Filled data'
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        # return redirect('home')
    except Exception as e:
        response_data['status'] = False
        response_data['message'] = 'something went wrong'
    return render(request, 'blog/home.html', {'form': form})

def note_edit(request, pk):
	note = Notes.objects.get(id=pk)
	print("note = ",note)
	# form = update_note_form(request.POST)
	# for name, value in request.POST.items()
	return render(request, 'blog/note_update.html', {'note':note})

class note_update(UpdateView):
	def post(self, request, *args, **kwargs):
		response_data = {}
		response_data['status'] = False
		if kwargs.get('pk', None):
			try:
				pk = kwargs.get('pk', None)
				obj = Notes.objects.get(pk=pk)
				obj.title = request.POST.get('title')
				obj.description = request.POST.get('description')
				obj.is_pinned = request.POST.get('is_pinned')
				obj.color = request.POST.get('color')
				obj.save()
				response_data['status'] = True
				response_data['message'] = "Updated Successfully"
			except Exception(DoesNotExist):
				response_data['message'] = "Note doesnt exists"
			except Exception as e:
				response_data['message'] = 'something went wrong'
		else:
			response_data['message'] = "Missing note identifier (id)"
		return HttpResponse(json.dumps(response_data), content_type='application/json')

	def get(self, request, *args, **kwargs):
		print("in get call")
		response_data = {}
		for name, value in request.POST.items():
			print("name = ",name)   #dict.items()
			Notes(**dict( [ (name, value) ] )).save()
		response_data['status'] = False
		response_data['message'] = "Note not found.."
		return HttpResponse(json.dumps(response_data), content_type='application/json')

def note_delete(request, pk):
	note = Notes.objects.get(id=pk)
	print("note = ",note)
	return render(request, 'blog/note_delete.html', {'note':note})
	# model = Notes
	# template_name = 'note_delete.html'
	# success_url = reverse_lazy('home')

class note_delete_note(DeleteView):
	def post(self, request, *args, **kwargs):
		response_data = {}
		response_data['status'] = False
		if kwargs.get('pk', None):
			try:
				pk = kwargs.get('pk', None)
				obj = Notes.objects.get(pk=pk)
				print("obj = ",obj)
				obj.delete()
				response_data['status'] = True
				response_data['message'] = "Deleted Successfully"
			except self.Notes.DoesNotExist:
				response_data['message'] = "Note doesn't exists"
			except Exception as e:
				response_data['message'] = 'something went wrong'
		else:
			response_data['message'] = "Missing note identifier (id)"
		return HttpResponse(json.dumps(response_data), content_type='application/json')


class note_unpinned(ListView):
	model = Notes
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class note_pinned(UpdateView):
	model = Notes
	fields = ['is_pinned']
	template_name = 'blog/note_pinned.html'

class note_archived(UpdateView):
	model = Notes
	fields = ['is_archived']
	template_name = 'blog/note_archived.html'

def note_lable(request, pk):
	note = Notes.objects.get(id=pk)
	return render(request, 'blog/note_lable.html', {'note':note})
	# model = Notes
	# fields = ['label']
	# template_name = 'note_lable.html'

class note_lable_note(UpdateView):
		def post(self, request, *args, **kwargs):
			response_data = {}
			response_data['status'] = False
			if kwargs.get('pk', None):
				try:
					pk = kwargs.get('pk', None)
					obj = Notes.objects.get(pk=pk)
					obj.label = request.POST.get('label')
					obj.save()
					response_data['status'] = True
					response_data['message'] = "Labeled Successfully"
				except Exception(DoesNotExist):
					response_data['message'] = "Note doesnt exists"
				except Exception as e:
					response_data['message'] = 'something went wrong'
			else:
				response_data['message'] = "Missing note identifier (id)"
			return HttpResponse(json.dumps(response_data), content_type='application/json')

class note_reminder(CreateView):
	model = Notes
	form = reminder_form
	fields = ['mydate']
	template_name = 'blog/note_reminder.html'

class note_colaborator(UpdateView):
	model=Notes
	fields=['collaborate']
	template_name = 'blog/note_collaborate.html'


# def home(request):
#     """
#
#     :param request: for all post or fandoo notes
#     :return: home page
#     """
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)
#
#
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#
#
# class PostDetailView(DetailView):
#     model = Post
#
#
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         # return super().form_valid(form)
#
#
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         """
#
#         :param form: If form is valid create instance
#         :return: form
#         """
#         form.instance.author = self.request.user
#         # return super().form_valid(form)
#
#     def test_func(self):
#         """
#
#         :return: check request and return true or false
#         """
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'
#
#     def test_func(self):
#         """
#
#         :return:
#         """
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# def about(request):
#     """
#
#     :param request:
#     :return: about.html page
#     """
#     return render(request, 'blog/about.html', {'title': 'About'})
