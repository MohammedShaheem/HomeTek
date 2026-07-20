from django.urls import path
from .views import HomeView,BlogListView,HotProductsByCategoryView

urlpatterns = [
    path("",HomeView.as_view(),name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('ajax/hot-products/', HotProductsByCategoryView.as_view(), name='hot_products_by_category'),

]