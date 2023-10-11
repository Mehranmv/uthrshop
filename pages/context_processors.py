from .models import Slider


def global_context(request):
    context = {
        'categories': Slider.objects.all(),
    }
    return context
