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

## Instalación de MongoDB

Si aún no tienes MongoDB instalado, sigue las instrucciones según tu sistema operativo:

### macOS

```bash
# Instalar MongoDB usando Homebrew
brew tap mongodb/brew
brew install mongodb-community
```

### Windows

1. Descarga el instalador desde [MongoDB Community Download Center](https://www.mongodb.com/try/download/community)
2. Ejecuta el instalador `.msi`
3. Selecciona "Complete" installation
4. Marca la opción "Install MongoDB as a Service"
5. Deja las opciones por defecto y completa la instalación

### Linux (Ubuntu/Debian)

```bash
# Importar la clave pública GPG de MongoDB
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

# Crear el archivo de lista de fuentes
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
   sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Actualizar el índice de paquetes e instalar
sudo apt-get update
sudo apt-get install -y mongodb-org
```

### Verificar la instalación

Después de instalar, verifica que MongoDB esté correctamente instalado:

```bash
mongod --version
```

## Gestión del Servicio MongoDB

### macOS

**Iniciar el servicio:**
```bash
brew services start mongodb-community
```

**Detener el servicio:**
```bash
brew services stop mongodb-community
```

**Reiniciar el servicio:**
```bash
brew services restart mongodb-community
```

**Verificar el estado:**
```bash
brew services list | grep mongo
```

**Iniciar manualmente (sin servicio):**
```bash
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

### Windows

Si instalaste MongoDB como servicio (opción por defecto), el servicio inicia automáticamente. Para controlarlo manualmente:

**Iniciar el servicio:**
```powershell
net start MongoDB
```

**Detener el servicio:**
```powershell
net stop MongoDB
```

**Verificar el estado:**
```powershell
sc query MongoDB
```

### Linux

**Iniciar el servicio:**
```bash
sudo systemctl start mongod
```

**Detener el servicio:**
```bash
sudo systemctl stop mongod
```

**Reiniciar el servicio:**
```bash
sudo systemctl restart mongod
```

**Verificar el estado:**
```bash
sudo systemctl status mongod
```

**Habilitar inicio automático:**
```bash
sudo systemctl enable mongod
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
