from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1 style='text-align:center; color:blue;'›Using Class Based Views</h1>")