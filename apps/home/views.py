from django.views.generic import TemplateView,ListView
from ..products.models import Collection,Category,Product
from .models import BlogPost
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['collections'] = Collection.objects.filter(is_active=True).order_by('-id')
        ctx['categories'] = Category.objects.filter(is_active=True).order_by('name')
        ctx['featured_products'] = (
            Product.objects.filter(is_active=True, category__is_active=True)
            .select_related('category','collection')
            .prefetch_related('images')
            .order_by('-created_at')[:12]
        )
        return ctx
    
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 9
    queryset = BlogPost.objects.all()


