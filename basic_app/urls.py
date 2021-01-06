from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^Profile/change_password/$', views.change_password, name='change_password'),
    url(r'^Profile/change_email/$', views.ChangeEmailView, name='change_email'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^consultation/$', views.consultation, name='consultation'),
    url(r'^consultation/cost_chat/$', views.cost_chat, name='cost_chat'),
    url(r'^consultation/free_chat/$', views.free_chat, name='free_chat'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^font_changing/$', views.font_changing, name='font_changing'),
    url(r'^Videos/$', views.Videos, name='Videos'),
    url(r'^Videos/Sport/$', views.Sport, name='Sport'),
    url(r'^Videos/stand_up_comedy/$', views.stand_up_comedy, name='stand_up_comedy'),
    url(r'^Videos/motivation/$', views.motivation, name='motivation'),
    url(r'^settings/Review/$', views.Review, name='Review'),
    url(r'^about/$', views.about, name='about'),
    url(r'^consultation/QA/$', views.QA, name='QA'),
    url(r'^Profile/$', views.Profile, name='Profile'),
    url(r'^Profile/Video_repository/$', views.Video_repository, name='Video_repository'),

     url(r'^successView/$', views.successView, name='successView'),

]
