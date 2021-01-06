from django.conf.urls import url
from django.urls import include, path

from . import views

#Gabi


app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Profile/change_password/$', views.change_password, name='change_password'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^consultation/$', views.consultation, name='consultation'),
    url(r'^consultation/cost_chat/$', views.cost_chat, name='cost_chat'),
    url(r'^consultation/cost_chat/Expert_questions$', views.Expert_questions, name='Expert_questions'),

    url(r'^consultation/free_chat/$', views.free_chat, name='free_chat'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^font_changing/$', views.font_changing, name='font_changing'),

    url(r'^Videos/$', views.Videos, name='Videos'),

    url(r'^Videos/Sport/$', views.video_Sport, name='Sport'),
    url(r'^Videos/sport/add_sport_video/$', views.add_sport_video, name='add_sport_video'),
    path('Videos/sport/sport_detail/<int:id>/', views.sport_detail, name='sport_detail'),
    path('Videos/sport/edit_sport/<int:id>/', views.edit_sport, name='edit_sport'),
    path('Videos/sport/delete_sport/<int:id>/', views.delete_sport, name='delete_sport'),


    url(r'^Videos/stand_up_comedy/$', views.video_stand_up, name='stand_up_comedy'),
    url(r'^Videos/stand_up_comedy/add_stand_up_video/$', views.add_stand_up_video, name='add_stand_up_video'),
    path('Videos/stand_up_comedy/stand_up_detail/<int:id>/', views.stand_up_detail, name='stand_up_detail'),
    path('Videos/stand_up_comedy/edit_stand_up/<int:id>/', views.edit_stand_up, name='edit_stand_up'),
    path('Videos/stand_up_comedy/delete_stand_up/<int:id>/', views.delete_stand_up, name='delete_stand_up'),

    url(r'^Videos/motivation/$', views.video_motivation, name='motivation'),
    url(r'^Videos/motivation/add_motivation_video/$', views.add_motivation_video, name='add_motivation_video'),
    path('Videos/motivation/motivation_detail/<int:id>/', views.motivation_detail, name='motivation_detail'),
    path('Videos/motivation/edit_motivation/<int:id>/', views.edit_motivation, name='edit_motivation'),
    path('Videos/motivation/delete_motivation/<int:id>/', views.delete_motivation, name='delete_motivation'),



    url(r'^settings/Review/$', views.Review, name='Review'),
    url(r'^about/$', views.about, name='about'),

    url(r'^Profile/Video_repository/$', views.Video_repository, name='Video_repository'),
    url(r'^settings/Review/success/$', views.successView, name='successView'),
    url(r'^consultation/Daliy_Tip/$', views.Daliy_Tip, name='Daliy_Tip'),
    url(r'^consultation/Daliy_Tip/Daliy_Tip_add/$', views.Daliy_Tip_add, name='Daliy_Tip_add'),
    path('consultation/Daliy_Tip/tip_detail/<int:id>/', views.tip_detail, name='tip_detail'),
    path('consultation/Daliy_Tip/edit_tip/<int:id>/', views.edit_tip, name='edit_tip'),
    path('consultation/Daliy_Tip/delete_tip/<int:id>/', views.delete_tip, name='delete_tip'),
    path('basic_app/settings/Profile/<int:id>/', views.profile, name='profile'),

    url(r'^consultation/QA/$', views.QA, name='QA'),
    url(r'^consultation/QA/QA_add/$', views.QA_add, name='QA_add'),
    path('consultation/QA/QA_detail/<int:id>/', views.QA_detail, name='QA_detail'),
    path('consultation/QA/edit_QA/<int:id>/', views.edit_QA, name='edit_QA'),
    path('consultation/QA/delete_QA/<int:id>/', views.delete_QA, name='delete_QA'),

    path('stories/detail/<int:id>/', views.detail, name='detail'),
    path('stories/edit_story/<int:id>/', views.edit_story, name='edit_story'),
    path('delete_story/<int:id>/', views.delete_story, name='delete_story'),


]
