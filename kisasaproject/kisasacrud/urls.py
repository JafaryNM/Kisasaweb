from importlib.resources import path


from django.urls import path
from .views import *

urlpatterns = [
     path('test/', IndexTemplate.as_view(), name='index_page'),
     path('post/', PostView.as_view(), name='post_view'),
     path('addpost/', AddPost.as_view(), name='addpost'),
     path('<slug:slug>/', SingleView.as_view(), name='single_post')
     
  ]
 