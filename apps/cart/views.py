from django.views.generic import CreateView

from .cart import Cart
from apps.shop.models import Product
from django.contrib import messages
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404


class CartAddItem(CreateView):
    form_class = CartAddProductForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs["product_id"])

    def form_valid(self, form):
        cart = Cart(self.request)
        cd = form.cleaned_data
        cart.add(
            product=self.get_object(),
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
        return HttpResponse(
            messages.success(
                self.request,
                f"'{self.get_object().name}' has been added to your bag"
            )
        )


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
        return HttpResponse(messages.success(request, f"'{product.name}' has been added to your bag"))
    else:
        return HttpResponse(messages.error(request, "Item wasn't added to your bag"))


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
    # return HttpResponse(render(request, 'snippets/cartitems.html', {'cart': cart}))


def cart_items(request):
    cart = Cart(request)
    return render(request, 'snippets/cartitems.html', {'cart': cart})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart-details.html', {'cart': cart})
