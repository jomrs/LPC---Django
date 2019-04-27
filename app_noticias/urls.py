from django.urls import path
from .views import HomePageView, detalhes, noticias_resumo, noticias_resumo_template, noticia_detalhes, slug_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', detalhes, name='fullpost'),
    path('noticias/<int:noticia_id>', noticia_detalhes, name="detalhes"),
    path('noticias/resumo/', noticias_resumo, name='resumo'),
    path('noticias/resumo2/', noticias_resumo_template, name='resumo2'),
    path('noticias/<str:pk>', slug_view, name='slug')
]




