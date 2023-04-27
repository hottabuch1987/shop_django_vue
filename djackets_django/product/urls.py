
from django.urls import path, include

from product import views
from rest_framework.routers import SimpleRouter

from product.views import LatestProductsList

router = SimpleRouter()
router.register(r'latest-products', LatestProductsList)

urlpatterns = [
    # path('latest-products/', views.LatestProductsList.as_view({'get': 'list'})),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
