from django.contrib import admin
from .models import Cliente, Produto


class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'preco', 'estoque')
	list_filter = ('estoque',)


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
