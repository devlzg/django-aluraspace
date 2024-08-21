# comando para iniciar um novo projeto: python manage.py startproject

# comando para criar um novo app: python manage.py startapp nome_do_app
  ## um app pode fazer parte de vários projetos

# é importante isolar as rotas de cada aplicativo, para manter o código mais organizado

# comando para coletar arquivos estáticos: python manage.py collectstatic

# é necessário colocar todos os apps novos no "INSTALLED_APPS" do settings.py

# tem duas pastas static, uma dentro de setup e uma fora. a de dentro do setup é para o produto em desenvolvimento, a outra é para quando estiver em produção, ou seja, durante o desenvolvimento so adicionamos arquivos à pasta dentro de setup, a de fora é responsabilidade do framework, após o comando collectstatic

# toda vez q alterarmos um model tem que usar o comando python manage.py makemigrations e depois migrate
# O comando makemigrations cria novas migrações com base nas alterações detectadas nos modelos.
# O comando migrate sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações.

# É necessário passar a classe ListandoFotografias no momento que registramos o app, como segundo argumento: admin.site.register(Fotografia, ListandoFotografias).