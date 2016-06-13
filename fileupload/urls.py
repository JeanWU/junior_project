# encoding: utf-8
from django.conf.urls import patterns, url
from fileupload.views import PictureCreateView, PictureDeleteView, PictureListView
from django.contrib.auth.decorators import login_required



urlpatterns = patterns('',
    #url(r'^basic/$', BasicVersionCreateView.as_view(), name='upload-basic'),
    #url(r'^basic/plus/$', BasicPlusVersionCreateView.as_view(), name='upload-basic-plus'),
    url(r'^(\d)/$', login_required(PictureCreateView.as_view()), name='upload-new'),
    #url(r'^(\d)/$', PictureCreateView, name='upload-new'),
    #url(r'^angular/$', AngularVersionCreateView.as_view(), name='upload-angular'),
    #url(r'^jquery-ui/$', jQueryVersionCreateView.as_view(), name='upload-jquery'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
)
