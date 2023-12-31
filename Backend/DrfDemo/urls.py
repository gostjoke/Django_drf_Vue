"""DrfDemo URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from viewApp.views import *

## path dont use Regular expression, 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include("app01.urls")),
    path('authors/', AuthorView.as_view()),
    re_path("authors/(\d+)", AuthorDetailView.as_view()), # 可用來捕獲主鍵

    ### publishes
    # path('publishes/', PublishView.as_view()),
    # # url: publishes/1  get(request, pk=1)
    # re_path("publishes/(?P<pk>\d+)", PublishDetailView.as_view()),

    ### only use one view
    path('publishes/', PublishView.as_view({"get":"list","post":"create"})),
    # # url: publishes/1  get(request, pk=1)
    re_path("publishes/(?P<pk>\d+)", PublishView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),
]
