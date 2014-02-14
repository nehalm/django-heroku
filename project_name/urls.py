
__author__ = 'file_author'

# Standard Library Imports

# Core Django Imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Third Party Imports

# App Imports
from core.views import IndexTemplateView


urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

                       # Index
                       url(
                           regex=r'^$',
                           view=IndexTemplateView.as_view(),
                           name='home'
                       ),
)
