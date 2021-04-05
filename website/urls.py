from django.urls import path, include

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:action>/<int:video_id>', views.getVideoID, name='getVideoID'),
    path('<int:video_id>/', views.playvideo, name='playvideo'),
]