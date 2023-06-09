<h1 align="center">API Demon-Slayer</h1>
<h3 align="center">Este proyecto esta construido con el fin de centralizar toda informacion que aprendere sobre el framework FastApi</h3>

## Requirimientos para su uso

Python 3.7+

FastAPI esta basado en:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> para los elemnetos de la web
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> para los elementos de los datos

## Instalacion

<div class="termy">

```console
$ pip install fastapi

---> 100%
```

</div>

También vas a necesitar un servidor ASGI para producción cómo Uvicorn o Hypercorn. <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> or <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install uvicorn

---> 100%
```

## Clonar el repositorio

Para colonar este proyecto se requiere tener instalado Git y ejecutar el siguiente comando en la ruta donde va a tarbajar con el proyecto
```console
$ git clone https://github.com/EndoRodrigo/Demon-Slayer.git

---> 100%
```
## Dependencias

Para el manejo de dependencias usaremos entorno virtual y administrador de paquete PIP
```console
$ python -m venv env
$ env\Scripts\activate  --> Windows
$ source env/bin/activate  --> Linux
$ pip install -r dependencias.txt
---> 100%
```

## Documentación interactiva de la API

En el siguiente link puedes probar tus Api sin necesidad de depender de otra herramientas como Postman o SopaIU solo debes iniciar el servidor de uvicorn 

```console
uvicorn main:app --reload --port 5000
http://127.0.0.1:5000/docs#/
---