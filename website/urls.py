from django.urls import path, include

from website import views

urlpatterns = [
    #path('', views.homePage, name='homePage'),
    path('<int:video_id>/', views.playvideo, name='videoDetail')
]