from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category, generate_unique_slug
from .forms import ProductForm
from django.utils.text import slugify
from django.views import View

for p in Product.objects.filter(slug=''):
    p.slug = generate_unique_slug(p.name)
    p.save()

def generate_unique_slug(name):
    base_slug = slugify(name)
    slug = base_slug
    counter = 1

    while Product.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
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
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self.name)
        super().save(*args, **kwargs)

    

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


