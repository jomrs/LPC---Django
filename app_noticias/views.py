from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Noticia

class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

def detalhes(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    return render(request, 'app_noticias/detalhes.html', {'detalhes': post})
