from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductsView.as_view(), name="products"),
    path("upload/", views.ProductUploadViewList.as_view(), name="upload_product"),  # 👈 این باید بیاد بالا
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
]
