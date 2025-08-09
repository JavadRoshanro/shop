from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils.text import slugify
from utils import IsAdminUserMixin
from . import tasks
from .models import Product, Category
from .forms import ProductForm


class HomeView(View):
    template_name = "base.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewIndex(View):
    template_name = "home/index.html"

    def get(self, request):
        title = {}
        return render(request, self.template_name, {'title': title})


class BucketHomeView(IsAdminUserMixin, View):
    template_name = "home/bucket.html"

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {"objects": objects})


class DeleteBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, "Your Delete Object The Perfect ... ")
        return redirect("home:bucket")


class DownloadBucketObjectView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, "Your Download Perfect File ...", "info")
        return redirect("home:bucket")


class ProductsView(View):
    template_name = "home/products.html"

    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, self.template_name, {'products': products, 'categories': categories})
       


class ProductDetailView(View):
    template_name = "home/product_detail.html"

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, self.template_name, {'product': product})


class ProductUploadViewList(View):
    template_name = "home/upload_product.html"

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()
            return redirect('home:product_detail', slug=product.slug)
        return render(request, self.template_name, {'form': form})
