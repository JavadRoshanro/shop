from django.urls import path, include
from . import views

app_name = "home"

bucket_url = [
    path("", views.BucketHomeView.as_view(), name="bucket"),
    path("delete_obj/<path:key>/", views.DeleteBucketObject.as_view(), name="delete_obj_bucket"),
    path("download_obj/<path:key>/", views.DownloadBucketObjectView.as_view(), name="download_obj_bucket"),
]

products_url = [
    path("", views.ProductsView.as_view(), name="products"),
    path("category/<slug:category_slug>/", views.ProductsView.as_view(), name="category_filter"),
    path("upload/", views.ProductUploadViewList.as_view(), name="upload_product"),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
]

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("index/", views.ViewIndex.as_view(), name="index"),
    path("bucket/", include(bucket_url)),
    path("products/", include(products_url)),
]
