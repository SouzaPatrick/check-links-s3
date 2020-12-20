# Realiza a checagem dos links da AWS S3

O script tem o intuito de agilizar um trabalho muito braçal que eu deveria fazer, trabalho esse que seria realizar a checagem de mais de 2800 links dentro de uma planilha, verificando quais nao era possivel verificar o material disponibilizado.

Sendo assim tive a ideia de criar esse script para fazer essa checagem.

##### Obs 1: Todos os arquivos estavam sendo disponibilizados em um bucket no S3.
##### Obs 2: Todos os testes foram realizados em um SO Windows 10 no powershell, caso use outro realize as devidas adaptacoes.

---

### Ele funciona basicamente nos seguintes passos:
- Passo 1 - Extrair os links do arquivos CSV
- Passo 2 - Realizar o get no link
- Passo 3 - Analisar a resposta obtida, especificamente o header da requisicao

---

### Inicializando a aplicacao
Passo 1: Crie um ambiente virtual para nao comprometer suas bibliotecas python (Projeto em Python 3):

```
# python -m virtualenv venv
```

Passo 2 - Acesse seu ambiente virtual
```
# .\venv\Scripts\activate:
```
#### Obs: Para desativar a venv basta digitar: deactivate

Passo 3 - Instale as dependencias:
```
# pip install -r requirements.txt
```

Passo 4 - Inicie o codigo
```
# python run.py
```

