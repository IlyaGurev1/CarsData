from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView


def main_page(request):
    return render(request, 'main/main.html')


class News(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/news.html')


class About(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['text'] = 'На сайте описаны характеристики различных моделей.'
        return context


