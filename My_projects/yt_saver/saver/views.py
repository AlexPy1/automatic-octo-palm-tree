from django.shortcuts import render
from pytube import YouTube
from yt_saver.settings import STATIC_ROOT
from .forms import PostForm


def save_video(request):
    res = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['v_url']
            yt = YouTube(link)
            ys = yt.streams.get_highest_resolution()
            ys.download(STATIC_ROOT)
            res = 'Ready! ' + yt.title
            v_name = yt.title + '.mp4'
            pic = yt.thumbnail_url
            return render(request, 'saver/home.html', {'form': form, 'res': res, 'v_name': v_name, 'pic': pic})
    else:
        form = PostForm()

    return render(request, 'saver/home.html', {'form': form, 'res': res})


