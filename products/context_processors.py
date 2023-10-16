from .models import Category


def global_context(request):
    context = {
        'category': Category.objects.all(),
    }
    return context
