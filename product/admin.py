from django.contrib import admin

from product.models import Category, Comment, Product, Tag

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
