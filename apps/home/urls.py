from django.urls import path
from .views import HomeView,BlogListView

urlpatterns = [
    path("",HomeView.as_view(),name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),

]