from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import source.views


urlpatterns = [
    path("", source.views.index, name="index"),
    path("admin/", admin.site.urls),
]
