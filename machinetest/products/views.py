from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    stock_value = sum([p.find_total_value() for p in products])
    return render(request, 'products/product_list.html', {'products': products, 'stock_value': stock_value})        

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})
    
# Create your views here.
