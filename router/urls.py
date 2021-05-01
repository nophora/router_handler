"""zips URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import createProfile_view, getProfile_view, sendrequest_view, createpost_view, info_view, hideauth_view, deletepost_view, getpost_view, ratepost_view, sharepost_view, comment_reply_view, rate_comment_view, rate_reply_view

urlpatterns = [
    path('', info_view),
    path('profilepost', createProfile_view),
    path('hideauth', hideauth_view),
    path('profileget', getProfile_view),
    path('sendrequest', sendrequest_view),
    path('createpost', createpost_view),
    path('deletepost', deletepost_view),
    path('getpost', getpost_view),
    path('ratepost', ratepost_view),
    path('sharepost', sharepost_view),
    path('commentreply', comment_reply_view),
    path('ratecomment', rate_comment_view),
    path('ratereply', rate_reply_view),
    path('admin/', admin.site.urls),

]
