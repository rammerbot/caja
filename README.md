##### Español:
### Sistema Cajas  
<div align="center">
<img src="https://employee.rammerbot.com/static/img/espacio2.jpg" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Sistema para centralizar Flujo de reportes diarios</div>  
  #### Descripcion.
  
> El Sistema Caja está diseñado para una empresa con sucursales que realizan actividades de ventas reflejadas en múltiples plataformas. Cada plataforma genera diferentes reportes y balances diarios.

#### Características
- Recolección de Reportes: El sistema facilita la recolección de diferentes reportes diarios y los carga directamente al servidor de la empresa.
- Operación Dinámica y Sin Errores: El sistema está diseñado para realizar la tarea de manera dinámica, sencilla, personalizada por empleado y libre de errores.
- Acceso Administrativo: Acceso a través de una cuenta administrativa para evaluar los reportes cargados al sistema mediante una interfaz sencilla y amigable.
- Generación de Reportes: Elaborar reportes y balances por fechas.

#### Instalación

##### Crear entorno virtual:
```
python -m venv caja
```

##### Entrar en el entorno
```
cd caja
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd caja/Script
```
```
activate
```
> en Lunix:
```
source caja/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/caja.git
```

> Navegar al directorio del proyecto:

```
cd caja
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Caja System
<div align="center">
<img src="https://employee.rammerbot.com/static/img/espacio2.jpg" align="center" style="width: 100%" />
</div>  
<div align="center">System for Centralizing Daily Report Flow</div>

 ### Description
 
 > The Caja System is designed for a company with branches that conduct sales activities reflected on multiple platforms. Each platform generates different daily reports and balances.

#### Features

- Report Collection: The system facilitates the collection of different daily reports and uploads them directly to the company's server.
- Dynamic and Error-Free Operation: The system is designed to perform the task dynamically, simply, customized per employee, and free of errors.
- Administrative Access: Access through an administrative account to evaluate the reports uploaded to the system via a simple and user-friendly interface.
- Report Generation: Generate reports and balances by date.

#### Installation
#### Create a virtual environment:
 > Copiar código
```
python -m venv caja
```

#### Enter the environment
```
cd caja
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd caja/Scripts
```
```
activate
```
> Linux:
```
source caja/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/caja.git
```

> Navigate to the project directory:

```
cd caja
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
