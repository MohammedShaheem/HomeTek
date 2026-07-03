from django.urls import path
from . import views



urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('collections/<slug:slug>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name='by_category'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>/',views.ProductListView.as_view(),name='by_subcategory'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
]