from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import MenuItem
from django.views import View

class PageDetailView(View):
    template_name = 'app/page_detail.html'

    def get(self, request, slug):
        page = get_object_or_404(MenuItem, slug=slug)
        return render(request, self.template_name, {'page': page})
