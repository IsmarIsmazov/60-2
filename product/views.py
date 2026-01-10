from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .form import ProductFrom
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


def home(request):
    if request.method == "GET":
        return render(request, "base.html")


@login_required(login_url="/login/")
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(
            request, "products/product_list.html", context={"products": products}
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
