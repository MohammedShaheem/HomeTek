from django.views.generic import TemplateView,ListView
from ..products.models import Collection,Category,Product
from .models import BlogPost
from ..aboutus.models import VisionMission,CompanyProfile,WhyChooseUs
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['collections'] = Collection.objects.filter(is_active=True).order_by('-id')
        ctx['categories'] = Category.objects.filter(is_active=True).order_by('name')

        # Default tab = first category, shown on initial page load
        active_category = ctx['categories'].first()
        ctx['active_category'] = active_category
        ctx['hot_products'] = (
            Product.objects.filter(is_active=True, category=active_category)
            .select_related('category', 'collection')
            .prefetch_related('images')
            .order_by('-created_at')[:4]
            if active_category else Product.objects.none()
        )

        ctx['featured_products'] = (
            Product.objects.filter(is_active=True, category__is_active=True)
            .select_related('category', 'collection')
            .prefetch_related('images')
            .order_by('-created_at')[:4]
        )
        ctx['company'] = CompanyProfile.objects.filter(is_active=True).first()
        ctx['vision_mission'] = VisionMission.objects.filter(is_active=True).first()
        ctx['why_choose_us'] = WhyChooseUs.objects.filter(is_active=True).order_by('order', 'id')[:3]
        

        return ctx
    
class HotProductsByCategoryView(TemplateView):
    """AJAX endpoint — returns rendered product cards for a given category."""

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        category = get_object_or_404(Category, id=category_id, is_active=True)

        products = (
            Product.objects.filter(is_active=True, category=category)
            .select_related('category', 'collection')
            .prefetch_related('images')
            .order_by('-created_at')[:4]
        )

        html = render_to_string(
            'partials/hot_product_items.html',
            {'products': products},
            request=request,
        )
        return JsonResponse({'html': html})
    
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 9
    queryset = BlogPost.objects.all()


