from django.conf.urls import patterns
from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path("admin/", include(admin.site.urls)),
)
