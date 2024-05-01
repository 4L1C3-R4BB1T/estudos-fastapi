```bash
# cria ambiente virtual
python -m venv <name>

# cria arquivo requirements.txt com as dependências do projeto
pip freeze > requirements.txt

# instala as dependências do projeto
pip install -r requirements.txt

# starta o server
uvicorn main:app

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# swagger 
http://127.0.0.1:8000/docs

# redoc
http://127.0.0.1:8000/redoc
```
