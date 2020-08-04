# FUSION

#### Aplicação: http://fusion-lfs.herokuapp.com
#### Travis-CI: https://travis-ci.com/github/souluanf/fusion-lfs

___
### Deploy Local
Criar e/ou ativar sua virtual env de preferência e instalar dependências:
```batch
pip install -r requirements.txt
```
Exportar a ENVIRONNT para defini o banco de daos a ser utilizado para o teste
``` batch
export ENVIRONMENT == 'test'
```
Criar a migração dos models para o banco
```batch
python manage.py mirate
```
Criar superusuário para gerenciar a aplicação
```batch
python manage.py createsuperuser
```
Rodar aplicação
```batch
python manage.py runserver
```
Aponte o browser para http://localhost:8000
___
### Testes
``` bash
coverage run manage.py test
```
#### Gerar relatório:
``` bash
coverage html
```
#### Ver relatório
``` bash
cd htmlcov/
python -m http.server
```
Aponte o browser para http://localhost:8000

#### Tradução

python manage.py makemessages -l es
python manage.py compilemessages
