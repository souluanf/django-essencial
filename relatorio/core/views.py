import io
from django.http import FileResponse
from django.views.generic import View

from reportlab.pdfgen import canvas
######
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Cria uma arquivo para receber os dados e gerar um pdf
        buffer = io.BytesIO()

        # Cria PDF
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 100, "Geek University")

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0)

        # Faz o DOwnload do arquivo em PDF gerado
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abre o pdf direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')


class Index2View(View):
    def get(self, request, *args, **kwargs):
        texto = ['Geek University', 'Evolua seu lado geek', 'Programação Web com Python e Django']
        html_String = render_to_string('relatorios.html', {'texto': texto})

        html = HTML(string=html_String)
        html.write_pdf(target='/tmp/relatorio2.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')

            #Faz o download do arquivo PDF
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf'

            #Abre o arquivo direto no browser
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf'
        return response
