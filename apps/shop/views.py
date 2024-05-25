from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Product


class HomePageView(TemplateView):
    template_name = 'index.html'


class ProductListView(ListView):
    template_name = "product/productslist.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_queryset(self):
        if self.kwargs:
            return Product.objects.filter(
                available=True, slug__icontains=self.kwargs["category_slug"]
            )
        else:
            return Product.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()

        if self.kwargs:
            category = get_object_or_404(Category, slug=self.kwargs["category_slug"])
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

    # noinspection PyUnresolvedReferences
    def get_object(self, queryset=None):
        return Product.objects.get(
            available=True, pk=self.kwargs["id"], slug=self.kwargs["slug"]
        )

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("Product not found")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
