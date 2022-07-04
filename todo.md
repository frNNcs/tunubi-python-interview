# Todo

- [x] 1. Corregir el requirements >= 1.1.3 por actualizacion de versiones de jinja2 etc
- [x] 2. Linter estatico
  - [x] Aplicar pep8
  - [ ] Rutina de linter estatico, github wf ?
- [x] 3. Upgrade project Layout for scalability
- [x] 4. Preparar estructura mas robusta para la app. esto incluye models y views
  - [x] 4.2 Crear archivo separado para views
    - [x] 4.2.1 Separar por method
    - [x] 4.2.2 Informar errores
    - [ ] 4.2.3 Documentar api rest.
  - [x] 4.3 Model pools and answers.
    - [x] 4.3.1 Validate creation (Schemas) marshmallow
    - [x] 4.3.2 Models.
    - [ ] 4.3.3 Incorporar un base model que incluya metodos globales y la coneccion a la bdd
- [ ] 5. Agrear usuarios y algun metodo de token o jwt a los endpoints.
- [ ] 6. Testing
  - [ ] 6.1 Unit testing a los 2 modelos para la creacion y validacion de los mismos
  - [ ] 6.2 e2e testing para los endpoints que chequeen la validez de las entradas y salidas
- [ ] 7. Coverage ?
- [ ] 8. Paginate ?

## Comentarios

  1. Corregir la version de flask ya que a partir de la version 1.1.3 se actualizan las librerias dependientes.
  [b247de](https://github.com/frNNcs/tunubi-python-interview/commit/7ffd1bba7a6cfe9a889df67647e31362f15466c1)
  2. Se debera realiar un test estatico (flake8) para conseguir un codigo homogeneo y de facil lectura para todos los integrantes del equipo.
  [b247de](https://github.com/frNNcs/tunubi-python-interview/commit/b247de503b666058dcd1afec819916e14a45bed8)

  3. (3-4)  Se debera aplicar una reestructuracion de los archivos para prepararlo para una mayor escalabilidad y poder aplicar el patron mvc. Se debera crear al menos un archivo para los modelos, formularios de validacion y vistas. Se deberan aplicar convenciones de REST-FULL APIs para agilizar la incorporacion de los mismos.
  [e6828b](https://github.com/frNNcs/tunubi-python-interview/commit/e6828b6664c6ee240f037b522aaa3826f0f5c514) -
  [64d41d](https://github.com/frNNcs/tunubi-python-interview/commit/64d41dd9b9ad91fe25606f4607be28f26afae3ab) -
  [88d1f05](https://github.com/frNNcs/tunubi-python-interview/commit/88d1f059dcf961f0a15c4a7bc8a899156660deb3)
  6. Se deberia agregar un sistema de login y permisos para el acceso controlado a los endpoints.
