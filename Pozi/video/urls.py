from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'video'

urlpatterns = [

    url(r'^Sport/$', views.video_Sport, name='Sport'),
    url(r'^sport/add_sport_video/$', views.add_sport_video, name='add_sport_video'),
    path('sport/sport_detail/<int:id>/', views.sport_detail, name='sport_detail'),
    path('sport/edit_sport/<int:id>/', views.edit_sport, name='edit_sport'),
    path('sport/delete_sport/<int:id>/', views.delete_sport, name='delete_sport'),

    url(r'^stand_up_comedy/$', views.video_stand_up, name='stand_up_comedy'),
    url(r'^stand_up_comedy/add_stand_up_video/$', views.add_stand_up_video, name='add_stand_up_video'),
    path('stand_up_comedy/stand_up_detail/<int:id>/', views.stand_up_detail, name='stand_up_detail'),
    path('stand_up_comedy/edit_stand_up/<int:id>/', views.edit_stand_up, name='edit_stand_up'),
    path('stand_up_comedy/delete_stand_up/<int:id>/', views.delete_stand_up, name='delete_stand_up'),

    url(r'^motivation/$', views.video_motivation, name='motivation'),
    url(r'^motivation/add_motivation_video/$', views.add_motivation_video, name='add_motivation_video'),
    path('motivation/motivation_detail/<int:id>/', views.motivation_detail, name='motivation_detail'),
    path('motivation/edit_motivation/<int:id>/', views.edit_motivation, name='edit_motivation'),
    path('motivation/delete_motivation/<int:id>/', views.delete_motivation, name='delete_motivation'),

]
