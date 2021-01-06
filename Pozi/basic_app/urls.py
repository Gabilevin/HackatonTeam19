from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Profile/change_password/$', views.change_password, name='change_password'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^consultation/$', views.consultation, name='consultation'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^font_changing/$', views.font_changing, name='font_changing'),
    url(r'^Videos/$', views.Videos, name='Videos'),
    url(r'^settings/Review/$', views.Review, name='Review'),
    url(r'^about/$', views.about, name='about'),
    url(r'^Profile/Video_repository/$', views.Video_repository, name='Video_repository'),
    url(r'^settings/Review/success/$', views.successView, name='successView'),
    path('basic_app/settings/Profile/<int:id>/', views.profile, name='profile'),
    path('stories/detail/<int:id>/', views.detail, name='detail'),
    path('stories/edit_story/<int:id>/', views.edit_story, name='edit_story'),
    path('delete_story/<int:id>/', views.delete_story, name='delete_story'),
    path('login_report/', views.login_report, name="login_report"),
    path('Consumption_report/', views.Consumption_report, name="Consumption_report"),
    path('Recent_changes/', views.Recent_changes, name="Recent_changes"),
]
