from django.contrib import admin
from .models import Noticia, Pessoa, Tag, MensagemDeContato

@admin.register(Noticia, Pessoa, Tag)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(MensagemDeContato)
class MnesagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)
