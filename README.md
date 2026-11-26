# ae1bim-oct25-feb26
Nombre: Mateo Cazar Mendoza
Asignatura: Desarrollo Basado En Plataformas Web

# Sistema de Gestión de Red de Clínicas Veterinarias

Práctica de desarrollo en entorno local utilizando **Python**, **SQLite** y el ORM **SQLAlchemy**. El proyecto modela la operación de una red de clínicas veterinarias distribuidas en distintas ciudades y realiza consultas sobre los datos almacenados.

## Descripción del dominio y modelo de entidades

* **Clínica (`Clinica`):** representa una unidad de atención médica para mascotas. Registra identificador único, nombre comercial, dirección y médico veterinario responsable.
* **Consultorio (`Consultorio`):** espacio de atención dentro de una clínica. Almacena identificador, nombre o número y especialidad principal (como medicina general, cirugía o dermatología). Cada consultorio pertenece obligatoriamente a una sola clínica (`1:N` desde `Clinica`).
* **Veterinario (`Veterinario`):** profesional que realiza consultas, diagnósticos y tratamientos. Registra identificador, nombres y apellidos, correo electrónico y número de licencia profesional. Cada veterinario pertenece únicamente a un consultorio (`1:N` desde `Consultorio`).
* **Historia Clínica (`HistoriaClinica`):** registro de la atención brindada a una mascota. Guarda identificador, fecha de atención, diagnóstico principal, tratamiento prescrito y nombre de la mascota atendida. Cada historia clínica está asociada obligatoriamente al veterinario que la elaboró (`1:N` desde `Veterinario`).

## Estructura del proyecto

* `configuracion.py`: define la conexión a la base de datos SQLite (`engine` y `SessionLocal`).
* `crear_base_entidades.py`: declara los modelos ORM con SQLAlchemy, sus relaciones y crea las tablas en la base de datos.
* `poblar_base.py`: inserta datos de prueba coherentes en clínicas, consultorios, veterinarios e historias clínicas.
* `consulta_all.py`: recupera todas las clínicas mediante `.all()` y muestra cuántas historias clínicas tiene asociada cada una.
* `consulta_filter.py`: filtra registros aplicando `.filter()` según una condición específica.
* `consulta_order_by.py`: ordena resultados utilizando `.order_by()`.
* `consulta_or.py`: aplica condiciones alternativas mediante `or_()`.
* `consulta_and.py`: aplica condiciones conjuntas mediante `and_()`.

## Orden de ejecución en entorno local

1. Crear las tablas en SQLite:
   ```bash
   python crear_base_entidades.py
