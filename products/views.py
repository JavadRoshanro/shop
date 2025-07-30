from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category
from .forms import ProductForm
from django.utils.text import slugify
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.base import ContentFile
from django.views import View

# Create your views here.

class ProductsView(View):
    template_name = "products/products.html"
    
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})
    
class ProductDetailView(View):
    template_name = "products/product_detail.html"
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, self.template_name, {'product': product})
    
    

class ProductUploadViewList(View):
    template_name = "products/upload_product.html"

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()  # 🔥 اینجا خودش image رو به Arvan میفرسته
            return redirect('products:product_detail', slug=product.slug)
        return render(request, self.template_name, {'form': form})


