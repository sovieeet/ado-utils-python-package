# ado-python-package-template

Template que sirve para publicar un paquete con un módulo llamado `adoutils`.
Este tiene una dependencia de un paquete llamado

## Crea un archivo pyproject.toml

En la raíz de este repositorio debes crear un archivo `pyproject.toml`

## Agrega build system setuptools

Utiliza la guía oficial para agregar sistema de construcción (build system) con el [siguiente link](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) y elige la opción `setuptools`.

## Agrega la metadata

Utiliza la guía oficial para agregar la metadata del proyecto con el [siguiente link](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata
).

## Agrega dependencias

Instala en tu ambiente la dependencia `pipreqs` utilizando el siguiente comando:

```
pip install pipreqs
```

Luego en la raíz de tu repositorio ejecuta

```
pipreqs
```
y un archivo `requirements.txt` debe haber sido creado.

Agrega lo siguiente a la sección `[project]` de tu archivo `pyproject.toml`.

```toml
dependencies = [
   <AGREGA ACÁ EL CONTENIDO DE TU ARCHIVO REQUIREMENTS>
]
```

# Genera una distribución

Para crear la distribución en GitHub deberás publicar una carpeta `dist` con la librería lista. 
Para lograr esto debemos correr el comando:

```
python -m build
```

Esto creará la carpeta de distribución, y con esto ya podemos publicar el paquete y consumirlo desde otro repositorio.
