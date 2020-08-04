from django.test import TestCase

from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):
	def setUp(self):
		self.nome = 'Luan Fernandes'
		self.email = 'souluan@live.com'
		self.assunto = 'Teste'
		self.mensagem = 'Testando o formulário de contato'

		self.dados = {
			'nome': self.nome,
			'email': self.email,
			'assunto': self.assunto,
			'mensagem': self.mensagem
		}
		self.form = ContatoForm(data=self.dados)  # ContatoForm(request.POST)

	def test_send_mail(self):
		form1 = ContatoForm(data=self.dados)
		form1.is_valid()
		res1 = form1.send_mail()

		form2 = self.form
		form2.is_valid()
		res2 = form2.send_mail()

		self.assertEquals(res1, res2)
