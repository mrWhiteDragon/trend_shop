from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def main(request):
    featured_products = Product.objects.filter(is_featured=True, available=True)[:3]  # Берем 3 акционных товара
    return render(request, 'products/main.html', {
        'featured_products': featured_products
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/product_list.html', {
        'products': products, 'categories': categories,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    return render(request, 'products/product_detail.html', {'product': product})
