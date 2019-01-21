# In this url section we can navigate
# to different url or go to different path
# after defining their path.



from django.urls import path, include
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )
from . import views
from django.conf.urls import *


# urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),

    # path('', include('blog.urls')),
    # url('create/', views.create_note, name='create_note'),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list.as_view(), name = 'home'),
    # path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail'),
    # path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
    path('edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('update/<int:pk>/', views.note_update.as_view(), name='note_update'),
    # path('detail/<int:pk>/', views.note_details.as_view(),name='note_detail'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('delete_note/<int:pk>/', views.note_delete_note.as_view(), name='note_delete_note'),
    path('unpinned/<int:pk>/', views.note_unpinned.as_view(), name='note_unpinned'),
    path('pinned/<int:pk>/', views.note_pinned.as_view(), name='note_pinned'),
    path('archived/<int:pk>/', views.note_archived.as_view(), name='note_archived'),
    path('lable/<int:pk>/', views.note_lable, name='note_lable'),
    path('lable_note/<int:pk>/', views.note_lable_note.as_view(), name='note_lable_note'),
    path('reminder/<int:pk>/', views.note_reminder.as_view(), name='note_reminder'),
    path('collaborate/<int:pk>/', views.note_colaborator.as_view(), name='note_collaborate'),
]