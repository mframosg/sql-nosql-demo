# MongoDB CRUD Operations

Este proyecto demuestra operaciones CRUD básicas (Crear, Leer, Actualizar, Eliminar) con MongoDB usando Python.

## Requisitos Previos

- Python 3.6 o superior
- MongoDB Community Edition instalado
- Homebrew (para usuarios de macOS)

## Configuración del Entorno

1. **Clona el repositorio** (si aún no lo has hecho):
   ```bash
   git clone https://github.com/mframosg/sql-nosql-demo.git
   cd sql-nosql-demo
   ```

2. **Crea y activa un entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Gestión del Servicio MongoDB

### Iniciar el servicio de MongoDB

```bash
brew services start mongodb-community
```

### Detener el servicio de MongoDB

```bash
brew services stop mongodb-community
```

### Reiniciar el servicio de MongoDB

```bash
brew services restart mongodb-community
```

### Verificar el estado del servicio

```bash
brew services list | grep mongo
```

### Iniciar MongoDB manualmente (sin servicio)

Si prefieres no usar el servicio, puedes iniciar MongoDB manualmente con:

```bash
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

## Ejecutar la Aplicación

```bash
python crud_mongodb.py
```

## Estructura del Proyecto

- `crud_mongodb.py`: Implementación de operaciones CRUD con MongoDB
- `requirements.txt`: Dependencias del proyecto

## Configuración de la Base de Datos

Por defecto, la aplicación se conecta a `mongodb://localhost:27017/`, base de datos `escuela`, colección `estudiantes`. Puedes cambiar estos valores al instanciar `BaseDeDatos`:

```python
db = BaseDeDatos(nombre_bd="mi_bd", nombre_coleccion="mi_coleccion")
```

## ¿Qué hace la demo?

Al ejecutar el script, se recorren las cuatro operaciones CRUD en orden:

| Paso | Operación | Descripción |
|------|-----------|-------------|
| 1 | **CREATE** | Inserta dos estudiantes con distintas estructuras |
| 2 | **READ** | Lista todos los documentos y filtra por condición |
| 3 | **UPDATE** | Modifica la edad de un estudiante y verifica el cambio |
| 4 | **DELETE** | Elimina un estudiante y muestra los restantes |

> La colección se limpia al inicio de cada ejecución para que la demo sea reproducible.

## Solución de Problemas

### Error de conexión

Si recibes un error de conexión, verifica que el servicio de MongoDB esté en ejecución:

```bash
brew services list
```

### Puerto en uso

Si el puerto 27017 está en uso, puedes cambiar el puerto en la configuración de MongoDB o detener el proceso que lo esté utilizando.

## Recursos Adicionales

- [Documentación de MongoDB](https://www.mongodb.com/docs/)
- [Documentación de PyMongo](https://pymongo.readthedocs.io/)
