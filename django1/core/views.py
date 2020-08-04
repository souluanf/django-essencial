from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):
	# print(dir(request))
	context = {
		'curso': 'Programação Web com Django Framework',
		'outro': 'Django é massa',
		'produtos': Produto.objects.all()

		# 'logado': 'Usuario não logado' if str(request.user) == 'AnonymousUser' else 'Usuario logado'
	}
	return render(request, 'index.html', context)


def contato(request):
	return render(request, 'contato.html')


def produto(request, pk):
	context = {
		# 'produto': Produto.objects.get(id=pk)
		'produto': get_object_or_404(Produto, id=pk)
	}
	return render(request, 'produto.html', context)


def error404(request, exception):
	template = loader.get_template('404.html')
	return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
	template = loader.get_template('500.html')
	return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
