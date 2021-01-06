# """check URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

from django.contrib import admin
from django.template.backends import django
from django.urls import path, re_path, reverse_lazy
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from .views import render_pdf_view, render_pdf_login , UserListView


app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    url(r'^Profile/change_email/$', views.change_email, name='change_email'),
    url(r'^Profile/Video_repository/$', views.Video_repository, name='Video_repository'),
    path('basic_app/settings/Profile/<int:id>/', views.profile, name='profile'),
    url(r'^Profile/change_password/$', views.change_password, name='change_password'),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/change_password_by_email'
                                                            '/password_reset.html'),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/change_password_by_email'
                                                                '/password_reset_done.html')
         , name="password_reset_done"),
    path('password-reset-confirm/<uidb64>P<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/change_password_by_email'
                                                                   '/password_reset_confirm.html'),
         name="password_reset_confirm"),

    path('password-reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/change_password_by_email'
                                                                    '/password_reset_complete.html'),
         name="password_reset_complete"),

    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('Consumption_report/', views.Consumption_report, name="Consumption_report"),
    path('Recent_changes/', views.Recent_changes, name="Recent_changes"),
    path('',views.UserListView.as_view(),name = 'user-list-view'),

    path('test/',render_pdf_view,name='test-view'),
    path('test2/',render_pdf_login,name='test-view2'),

]
