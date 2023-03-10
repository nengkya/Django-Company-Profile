from django.urls import re_path, include
from django.contrib import admin

from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/',include("about.urls")),
    re_path(r'^service/',include('service.urls')),
    re_path(r'^product/',include('product.urls')),
    re_path(r'^portofolio/',include('portofolio.urls')),
    re_path(r'^blog/',include('blog.urls')),
    re_path(r'^$',views.index),
]
