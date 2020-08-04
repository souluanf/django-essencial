from django.contrib import admin

from .models import Cargo, Servico, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'ativo', 'atualizado_em')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
	list_display = ('servico', 'icone', 'ativo', 'atualizado_em')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cargo', 'ativo', 'atualizado_em')
