from django.urls import path, include
from . import views

app_name="home"



bucket_url = [
    path("", views.BucketHomeView.as_view(), name="bucket_home"),
    path("delete_obj_bucket/<path:key>/", views.DeleteBucketObject.as_view(), name="delete_obj_bucket")
]
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("index/", views.ViewIndex.as_view(), name="index" ),
    path("bucket/", include(bucket_url))
   
]