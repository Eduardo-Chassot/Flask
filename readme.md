Bom dia, professor!

Para instalar o Flask você precisa ter o python instalado, tenho certeza que tu ja tem então não vou explicar aqui!

Você precisa criar uma pasta, o nome tu mesmo decide, entra nela pelo cmd e digita
"-m venv my-venv"

Depois disso, digita

"my-venv\Scripts\activate"

Por ultimo digita "pip install Flask".

Esse ultimo comando vai instalar o flask no diretório, agora vamos declara qual arquivo o Flask vai ter como o servidor, como o meu arquivo é app.py, será então:
"set FLASK_APP=app.py"

Por ultimo vamos dar um "flask run" no cmd, logo aparecerá uma mensagem informando a URL para você acessar.