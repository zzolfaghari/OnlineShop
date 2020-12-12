from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list_by_category(request, category_slug=None):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request,
                  'order/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_list1(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request,
                  'order/product/list.html',
                  {
                      'categories': categories,
                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'order/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

# def category_list(request, category):
#     product = Product.objects.filter(category=category)
#     return HttpResponse(product)
