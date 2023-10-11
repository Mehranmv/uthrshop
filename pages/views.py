from django.shortcuts import render
from django.views import View


class IndexPageView(View):
    def get(self, request):
        return render(request, 'pages/index.html')
