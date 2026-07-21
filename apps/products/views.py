from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Product, Category, SubCategory, Collection
from ..aboutus.models import CompanyProfile
# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.filter(is_active=True)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company'] = CompanyProfile.objects.filter(is_active=True).first()
        return ctx

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12                              

    def get_queryset(self):
        qs = (
            Product.objects
            .filter(is_active=True, category__is_active=True)   
            .select_related('category', 'subcategory', 'collection')
            .prefetch_related('images')
        )

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)

        subcategory_slug = self.kwargs.get('subcategory_slug')
        if subcategory_slug:
            qs = qs.filter(subcategory__slug=subcategory_slug)

        return qs     
                                
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories']  = Category.objects.filter(is_active=True)
        ctx['collections'] = Collection.objects.filter(is_active=True)
        ctx['company'] = CompanyProfile.objects.filter(is_active=True).first()

        category_slug = self.kwargs.get('category_slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')

        category = None
        subcategory = None

        if category_slug:
            category = Category.objects.filter(slug=category_slug, is_active=True).first()
        if subcategory_slug:
            subcategory = SubCategory.objects.filter(slug=subcategory_slug).first()

        ctx['category'] = category                                    
        ctx['subcategory'] = subcategory
        ctx['active_category'] = category.slug if category else ''
        ctx['active_subcategory'] = subcategory.slug if subcategory else ''

        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'                       

    def get_queryset(self):
        return (
            Product.objects
            .filter(is_active=True, category__is_active=True)
            .select_related('category', 'subcategory', 'collection')
            .prefetch_related('images')
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.object

        ctx['related_products'] = (
            Product.objects
            .filter(
                category=product.category,
                is_active=True
            )
            .exclude(pk=product.pk)
            .prefetch_related('images')
            [:4]
        )

        ctx['images'] = product.images.all()

        ctx['primary_image'] = product.get_primary_image()

        return ctx
    

class CollectionListView(ListView):
    model = Collection
    template_name = 'products/collection_list.html'
    context_object_name = 'collections'
    queryset = Collection.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company'] = CompanyProfile.objects.filter(is_active=True).first()
        return ctx

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'products/collection_detail.html'
    context_object_name = 'collection'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Collection.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        collection = self.object

        ctx['products'] = (
            Product.objects
            .filter(
                collection=collection,
                is_active=True,
                category__is_active=True
            )
            .select_related('category', 'subcategory')
            .prefetch_related('images')
        )
        return ctx