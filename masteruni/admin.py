from django.contrib import admin
from .models import Etiqueta, Categoria, Ubicacion, Pieza, Kit, Conjunto, PiezaKit, PiezaConjunto

admin.site.register(Etiqueta)
admin.site.register(Categoria)
admin.site.register(Ubicacion)
admin.site.register(Pieza)
admin.site.register(Kit)
admin.site.register(Conjunto)
admin.site.register(PiezaKit)
admin.site.register(PiezaConjunto)
