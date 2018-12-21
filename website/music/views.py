# from django.http import Http404
# #from django.http import HttpResponse
# from .models import Album, Song
# #from django.template import loader
# from django.shortcuts import render, get_object_or_404
#
# # Create your views here.
#
#
# def index(request):
#     # all_albums = Album.objects.all()
#     # html = ''
#     #
#     # for album in all_albums:
#     #     url = ' /music/' + str(album.id) + '/'  #To search individual album with id
#     #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     # return HttpResponse(html)
#     #
#
#     all_albums = Album.objects.all()
#    # template = loader.get_template('music/index.html')
#
#     #make dictionay named context
#
#     # context ={
#     #     'all_albums': all_albums,
#     # }
#     #return HttpResponse(template.render(context, request))
#     return render(request, 'music/index.html',  {'all_albums': all_albums,})
#
#
# def detail(request, album_id):
#    # return HttpResponse("<h2> Details for album id:" + str(album_id) + "</h2>")
#    #  try:
#    #      album = Album.objects.get(pk=album_id)
#    #  except Album.DoesNotExist:
#    #      raise Http404("Album does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
# def favorite(request, album_id):
#     is_favorite = True
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExixt):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "you did not select valid song"
#
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})

from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'








