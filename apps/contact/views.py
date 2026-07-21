from django.views.generic import TemplateView
from .models import ContactUs


class ContactUsView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context["contact"] = ContactUs.objects.first()
        return context