# finapp/admin.py
from django.contrib import admin
from .models import Usuario, Balanco, Receita, Despesa, HistoricoBalanco

admin.site.register(Usuario)
admin.site.register(Balanco)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(HistoricoBalanco)
