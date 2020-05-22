"""stepik_toolbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from heroku_app.views import api_view, MyView, TCatView, LCatView, DetailCatView, template_cat, postcard_view, thanks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', api_view),
    path('api/', MyView.as_view()),
    path('t_cat/', template_cat),
    path('tcat/', TCatView.as_view()),
    #path('lcat/', LCatView.as_view()),
    url(r'^lcat/([\w-]+)/$', LCatView.as_view()),
    path('dcat/<int:pk>/', DetailCatView.as_view()),
    path('pcard/', postcard_view),
    path('thanks/', thanks_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
