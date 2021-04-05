from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from website.models import Video

def index(request):
    video_id = 1
    context = {
        'video_id': video_id,
    }
    return render(request, 'website/index.html', context)

def getVideoID(request, action, video_id):
    count = Video.objects.count()

    if action == 'next':
        if video_id >= count:
            video_id = 1
        else:
            video_id = video_id + 1

    elif action == 'prev':
        if video_id <= 1:
            video_id = count
        else:
            video_id = video_id - 1;

    video_item = Video.objects.get(pk=video_id)

    return HttpResponse(serializers.serialize('json', [ video_item, ]))

def playvideo(request, video_id):
    video_item = Video.objects.get(pk=video_id)

    context = {
        'video_item': video_item,
    }
    return render(request, 'website/videoPlayer.html', context)