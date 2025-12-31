from django.shortcuts import render

from .models import Product

# Create your views here.

"""
select * form product;
"""
# product = """
#     select * from product where name = '{user_input}';
# """
"""
select * from product ILIKE where = "%phone%"
"""


def home(request):
    return render(request, "base.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", context={"products": products})


def product_detail(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request, "products/product_detail.html", context={"product": product})


