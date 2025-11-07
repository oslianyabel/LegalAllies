from .models import HomeConfiguration, SocialNetwork


def global_settings(request):
    """
    Context processor para hacer disponibles variables globales en todos los templates.
    """
    return {
        'home_config': HomeConfiguration.objects.first(),
        'social_networks': SocialNetwork.objects.all(),
    }
