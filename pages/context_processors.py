from .models import Slider, Menu


def global_context(request):
    context = {
        'slider': Slider.objects.all(),
        'menu': Menu.objects.all()
    }
    return context
