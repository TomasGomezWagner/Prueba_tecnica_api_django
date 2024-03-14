# Prueba_tecnica_api_django
API realizada con Django REST framework para acceder a datos de vehiculos.

## Version Python
3.11.4

## Inicio
- Clonar el repositorio  
- Crear un entorno virtual e instalar los requerimiento utilizando el archivo requirements.txt: ```pip install -r requirements.txt```  
- Activar el entorno virtual: ```entorno_virtual/Scripts/activate```  
- Acceder a la carpeta backend.  
- Ejecutar el comando: ```python manage.py migrate```. Esto generara la base de datos (sqlite3) y las migraciones necesarias
para poder ejectutar la aplicacion.
- Los datos pueden ser generados o descargar [base de datos](https://drive.google.com/file/d/143exuw3TnX04nXNLXviXwMLa9KhDHv9r/view?usp=sharing) y reemplazar por la generada en el paso anterior.
- Ejecutar la aplicacion: ```python manage.py runserver```. Esto por defecto habilita la aplicacion en la ruta ```.http://127.0.0.1:8000/```.
- Si se elije crear los datos:
    - Crear superuser: ```python manage.py createsuperuser```(seguir los pasos que pide)
    - La forma mas facil es desde la vista crear los datos. Dirigirse a la ruta ```http://127.0.0.1:8000/admin``` y loguearse.
    Desde el panel se podra hacer todas las operaciones de CRUD.

## Rutas
### Autorizacion
### ```/api/auth/```  
Obtiene el token para la autentificacion.  

Metodo = POST  

BODY = {"username": username, "password" : password}  

Retorna = {"token": "403c650ffb332a5a183fa4e1c90d65fe9f9ab2e0"}

### Vehiculo Info

### ```/api/v0/vehiculos/```  
Lista todos los vehiculos. Por defecto los ordena por año de menor a mayor.  

Metodo = GET  

Acepta query parameters:  
- tipo  
    - ```http://127.0.0.1:8000/api/v0/vehiculos/?tipo=auto```  
- ordering: acepta los campos anio y precio  
    - ```http://127.0.0.1:8000/api/v0/vehiculos/?ordering=precio``` (puede ser descendente usando: -precio)
    - ```http://127.0.0.1:8000/api/v0/vehiculos/?ordering=anio``` (puede ser descendente usando: -anio)
- search: tipo
    - ```http://127.0.0.1:8000/api/v0/vehiculos/?search=auto```  

Si no se usa alguno de esos parametros devolvera la lista completa de vehiculos.

Retorna (ejemplo)
```
    [
        {
            "id": 1,
            "nombre": "etios",
            "tipo": {
                "id": 1,
                "descripcion": "auto"
            },
            "marca": {
                "id": 1,
                "descripcion": "Toyota"
            },
            "anio": 2022,
            "precio": 444000,
            "imagen": "etios.jpg",
            "ficha": {
                "titulo_principal": "Toyota Etios",
                "descrip_principal": "El mejor auto posible",
                "img_principal": "img_etios_principal.jpg",
                "titulo2": "Motor",
                "descrip2": "Es muy potente",
                "img_2": "img2_etios.jpg",
                "titulo3": "Compacto",
                "descrip3": "Facil de estacionar",
                "img_3": "img3_etios.jpg"
                }
        }
    ]
```

### Informacion de vehiculo en particular

### ```/api/v0/vehiculos/<int:pk>/```  
Obtiene la informacion de un vehiculo en particular.

Metodo = GET  

Retorna (ejemplo) 
``` 
{
            "id": 1,
            "nombre": "etios",
            "tipo": {
                "id": 1,
                "descripcion": "auto"
            },
            "marca": {
                "id": 1,
                "descripcion": "Toyota"
            },
            "anio": 2022,
            "precio": 444000,
            "imagen": "etios.jpg",
            "ficha": {
                "titulo_principal": "Toyota Etios",
                "descrip_principal": "El mejor auto posible",
                "img_principal": "img_etios_principal.jpg",
                "titulo2": "Motor",
                "descrip2": "Es muy potente",
                "img_2": "img2_etios.jpg",
                "titulo3": "Compacto",
                "descrip3": "Facil de estacionar",
                "img_3": "img3_etios.jpg"
                }
        }
```

### Update Vehiculo

### ```/api/v0/vehiculos/<int:pk>/update/```
Genera un update en la base de datos del vehiculo pedido, con los datos enviados.

Metodo = PUT

BODY = {
    "nombre": "etios",
    "tipo":1
    "marca": 1
    "anio": 2022,
    "precio": 444000,
    "imagen": "etios.jpg",
}

Puede tener uno o mas campos de los mostrados.  
Los campos 'tipo' y 'marca' son los id, no se envia la entidad completa como si se recibe.

### Delete Vechiculo

### ```/api/v0/vehiculos/<int:pk>/delete/```
Elimina un vehiculo

Metodo = DELETE

### Crear Vehiculo

### ```/api/v0/vehiculos/create/  ```
Crea un vehiculo. Los campos 'tipo' y 'marca' son los id, no se envia la entidad completa como si se recibe.

Metodo = POST

BODY = {
    "nombre": "etios",
    "tipo":1
    "marca": 1
    "anio": 2022,
    "precio": 444000,
    "imagen": "etios.jpg",
}

### Fichas

### ```/api/v0/vehiculos/fichas/```

Dependiendo del metodo usado lista o crea fichas de vehiculo.

Metodos  
- GET = lista todos los tipos de vehiculo
- POST = crea un tipo de vehiculo nuevo. 
    - Ej BODY  
        ```
        {   
            "nombre": 1,
            "titulo_principal": "Toyota Etios",  
            "descrip_principal": "El mejor auto posible",  
            "img_principal": "img_etios_principal.jpg",  
            "titulo2": "Motor",  
            "descrip2": "Es muy potente",  
            "img_2": "img2_etios.jpg",  
            "titulo3": "Compacto",  
            "descrip3": "Facil de estacionar",  
            "img_3": "img3_etios.jpg"  
        }
        ```  
El campo nombre es el nro de id de el vehiculo al que pertenece.


### Tipos

### ```/api/v0/vehiculos/tipos/```

Dependiendo del metodo usado lista o crea los tipos de vehiculo.

Metodos  
- GET = lista todos los tipos de vehiculo
- POST = crea un tipo de vehiculo nuevo. 
    - Ej BODY {"descripcion" : "camion"}

### Marcas

### ```/api/v0/vehiculos/marcas/```

Dependiendo del metodo usado lista o crea marcas.

Metodos  
- GET = lista todas las marcas.
- POST = crea una marca nueva. 
    - Ej BODY {"descripcion" : "Ferrari"}

