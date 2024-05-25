from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('menu', views.ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
