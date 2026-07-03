from .models import CompanyProfile

def company_profile(request):
    return{
        'site_company':CompanyProfile.objects.filter(is_active=True).first()
    }