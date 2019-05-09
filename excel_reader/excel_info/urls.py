from rest_framework import routers
from rest_framework.routers import SimpleRouter
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('upload_file',UploadView.as_view(),name='UploadView'),
    path('file_list',FileListView.as_view(),name='FileListView'),
    re_path('file_details/(?P<pk>\d+)/$',FileDetailsView.as_view(),name='file_details'),

]
router = SimpleRouter(trailing_slash=False)

urlpatterns += router.urls