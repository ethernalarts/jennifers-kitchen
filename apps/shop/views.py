from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Product


class ProductListView(ListView):
    template_name = "product/productslist.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.category = None
        self.category_slug = None

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()

        if self.category_slug:
            category = get_object_or_404(Category, slug=self.category_slug)
            products = products.filter(category=category)
            context["category"] = category

        context["products"] = products
        context["categories"] = Category.objects.all()

        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product/productdetail.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_object(self, queryset=None):
        return Product.objects.get(available=True)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("Product not found")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
