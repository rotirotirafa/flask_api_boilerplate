# WIP 

Passo a passo para configurar este projeto para desenvolvimento.

Instalar as dependencias necessárias com `pipenv install`

Ative o ambiente virtual com `pipenv shell`

### Configurar banco  de dados:
    - instale e crie um banco postgres
    - no arquivo .env substitua as informações postgresql://{db_user}:{db_password}@{address}:{port}/{db_name}
    
## Migrations
O SQLAlchemy com Flask Migrations é responsável por gerenciar as migrations no banco
    
Para iniciar a criação do banco inicie com ````python manage.py db init````

Para gerar uma versão de migrations ```python manage.py db migrate```

Para executar a operação ```python manage.py db upgrade```

Para fazer rollback ```python manage.py db downgrade```


# Run

```python app.py```