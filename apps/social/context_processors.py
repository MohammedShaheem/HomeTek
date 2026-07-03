from .models import SocialProfile


def social_profiles(request):
    return {
        'social_profiles': SocialProfile.objects.filter(is_active=True)
    }