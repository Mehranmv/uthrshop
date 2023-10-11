from .models import Slider


def global_context(request):
    context = {
        'slider': Slider.objects.all(),
    }
    return context
