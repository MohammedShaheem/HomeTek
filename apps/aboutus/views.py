from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CompanyProfile,VisionMission,WhyChooseUs
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company'] = CompanyProfile.objects.filter(is_active=True).first()
        ctx['vision_mission'] = VisionMission.objects.filter(is_active=True).first()
        ctx['why_choose_us'] = WhyChooseUs.objects.filter(is_active=True).order_by('order', 'id')[:3]

        return ctx