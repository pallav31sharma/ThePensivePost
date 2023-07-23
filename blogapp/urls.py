"""findinternship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home, post, category, create_post, update_post, delete_post, register_request,login_request,logout_request,get_my_articles

urlpatterns = [
                  path('home', home, name='home'),
                  path('blog/<slug:url>', post),
                  path('category/<slug:url>', category),
                  path('posts/', post),
                  path('update/<int:id>', update_post),
                  path('delete/<int:id>', delete_post),
                  path("", register_request, name="register"),
                  path("login", login_request, name="login"),
                  path("logout", logout_request, name="logout"),
                  path("myarticles", get_my_articles, name="myarticles"),
                  path('test', create_post),
                  path('tinymce/', include('tinymce.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
