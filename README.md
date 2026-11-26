# ae1bim-oct25-feb26
Nombre: Mateo Cazar Mendoza

Asignatura: Desarrollo Basado En Plataformas Web

Docente: Rene Elizalde Solano

# Sistema de Gestión de Red de Clínicas Veterinarias

Práctica de desarrollo en entorno local utilizando **Python**, **SQLite** y el ORM **SQLAlchemy**. El proyecto modela la operación de una red de clínicas veterinarias distribuidas en distintas ciudades y realiza consultas sobre los datos almacenados. El modelo contempla **Clínica**, **Consultorio**, **Veterinario** e **Historia Clínica**, donde cada **Consultorio** pertenece obligatoriamente a una sola **Clínica**, cada **Veterinario** pertenece a un único **Consultorio** y cada **Historia Clínica** está asociada obligatoriamente al **Veterinario** que la elaboró.

## Estructura del proyecto

* `configuracion.py` : define la conexión a la base de datos SQLite (`engine` y `SessionLocal`).
* `crear_base_entidades.py` : declara los modelos ORM con SQLAlchemy, sus relaciones y crea las tablas en la base de datos.
* `poblar_base.py` : inserta datos de prueba coherentes en clínicas, consultorios, veterinarios e historias clínicas.
* `consulta_all.py` : recupera todas las clínicas mediante `.all()` y muestra cuántas historias clínicas tiene asociada cada una.
* `consulta_filter.py` : filtra registros aplicando `.filter()` según una condición específica.
* `consulta_order_by.py` : ordena resultados utilizando `.order_by()`.
* `consulta_or.py` : aplica condiciones alternativas mediante `or_()`.
* `consulta_and.py` : aplica condiciones conjuntas mediante `and_()`.

