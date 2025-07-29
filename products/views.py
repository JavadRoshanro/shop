from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class ProductsView(View):
    template_name = "products/products.html"
    
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})