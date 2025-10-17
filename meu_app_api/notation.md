## Terminal (bash)

### Criar ambiente virtual
`python -m venv venv`

### Ativar ambiente virtual
`source venv/bin/activate`

### Executar o docker compose
`docker compose up -d`

### Conectar ao banco de dados no docker
`docker exec -it db_id psql -U db_user -d db_name`

#########

## Ambiente Virtual (venv)
### Instalar o Flask
`pip install Flask`

#### Verificar instalacao
`pip freeze`

### Instalar python-dotenv
`pip install python-dotenv`

### Instalar os driver do python 
`pip install psycopg2-binary python-dotenv`

### Se erro de pyscopg2.extrar.DictCursor instalar
`pip install psycopg2`

#########




