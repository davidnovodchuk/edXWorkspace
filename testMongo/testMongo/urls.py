from django.conf.urls import patterns, include, url
from testMongo import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testMongo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^upload/', views.upload_file, name='upload_file')
    #url(r'^admin/', include(admin.site.urls)),
)