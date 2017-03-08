from django.conf.urls import url
from django.contrib import admin
from .views import(
   #display_detail,
   #create,
   create



  )
urlpatterns= [
    url(r'^scholarships/$', create)
    #url(r'^create/$', post_create),
    #url(r'^(?P<id>\d+)/$', post_detail,name='detail'), # this is going to store the value extracted by the regex into id ?p<id>
    #url(r'^(?P<id>\d+)/edit/$', post_update,name='update'),
    #url(r'^(?P<id>\d+)/delete/$', post_delete),
    ]
