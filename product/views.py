from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .form import ProductFrom, SearchForm
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

"""
insert into product (name, description, price) values ('name', 'description', 100);
"""

# GET - для просмотра данных
# POST - для отправки данных
# PUT - для обновления данных
# PATCH - для обновления частичных данных
# DELETE - для удаления

# lt products.price < 100
# gt prodcuts.price > 100
# lte products.price <= 100
# gte products.price >= 100


def home(request):
    if request.method == "GET":
        return render(request, "base.html")


lsit = ["123", 12, "asd", True]
# lsit[start:stop:step]


@login_required(login_url="/login/")
def product_list(request):
    products = Product.objects.all()
    if request.method == "GET":
        limit = 3
        forms = SearchForm()
        search = request.GET.get("search")
        category = request.GET.get("category")
        tags = request.GET.getlist("tags")
        ordering = request.GET.get("ordering")
        page = request.GET.get("page") if request.GET.get("page") else 1
        if category:
            products = products.filter(category=category)
        if search:
            products = products.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        if tags:
            products = products.filter(tag__in=tags)

        if ordering:
            products = products.order_by(ordering)
        max_page = range(products.count() // limit + 1)
        products = products[limit * (int(page) - 1) : limit * int(page)]
        return render(
            request,
            "products/product_list.html",
            context={"products": products, "form": forms, "max_page": max_page[1:]},
        )


@login_required(login_url="/login/")
def product_detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.filter(id=product_id).first()
        return render(
            request, "products/product_detail.html", context={"product": product}
        )


@login_required(login_url="/login/")
def product_create_view(request):
    if request.method == "GET":
        form = ProductFrom()
        return render(request, "products/product_create.html", context={"form": form})
    elif request.method == "POST":
        form = ProductFrom(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                photo=form.cleaned_data["photo"],
            )
        return HttpResponse("Product created")
