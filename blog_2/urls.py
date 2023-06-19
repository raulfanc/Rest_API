"""
URL configuration for simpleblog_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog_2.views import index, post_list, post_detail, get_user_id
from blog_2.viewsets import PostViewSet, UserViewSet

# from blog_2.viewsets import PostList, PostDetail

router = DefaultRouter()
router.register("post", PostViewSet)
router.register('user', UserViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("home/", index),
    path('post/', post_list),
    path('post_detail/<int:id>/', post_detail),
    path('get_user_id/', get_user_id),
    # path('postlist/', PostList.as_view()),
    # path('postdetail/<int:id>/', PostDetail.as_view()),
]
