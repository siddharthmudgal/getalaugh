from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from website.models import Video


#landing page
def homePage(request):
    video_list = Video.objects.all()
    context = {
        'video_list':video_list,
    }

    return render(request, 'website/homepage.html',context)

def playvideo(request, video_id):
    video_item = Video.objects.get(pk=video_id)
    count = Video.objects.count()
    if video_id > 1:
        prev_video_item_id = video_id-1
    else:
        prev_video_item_id = count

    if video_id == count:
        next_video_item_id = 1
    else:
        next_video_item_id = video_id+1

    context = {
        'video_item': video_item,
        'prev_video_item_id': prev_video_item_id,
        'next_video_item_id': next_video_item_id,
    }
    return render(request, 'website/playvideo.html', context)