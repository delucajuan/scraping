
# Web Scraping de Quotes to Scrape 

## Descripción

Este proyecto realiza scraping de citas desde el sitio web [Quotes to Scrape](https://quotes.toscrape.com) y almacena la información extraída en una base de datos SQLite. El script navega a través de todas las páginas del sitio, extrae citas, autores y etiquetas, y guarda estos datos en una base de datos relacional con las tablas correspondientes.

## Archivos del Proyecto

- **main.py**: Archivo principal que coordina el flujo completo del proceso. Comprueba si la base de datos existe, y si no, la crea. Luego, realiza el scraping de las citas y almacena los datos en la base de datos.
  
- **create_db.py**: Script que define y crea la estructura de la base de datos (tablas de autores, citas, etiquetas, y relaciones entre ellas).

- **db.py**: Contiene las funciones necesarias para interactuar con la base de datos, incluyendo la creación de la conexión, inserción de autores, citas, etiquetas, y la asociación de citas con etiquetas.

- **scraper.py**: Se encarga de realizar el scraping de la página web. Navega a través de todas las páginas disponibles, extrae la información necesaria (citas, autores, etiquetas), y la organiza para ser almacenada. Incluye un manejo de errores HTTP comunes y evita sobrecargar el servidor mediante pausas aleatorias entre solicitudes.

- **get_quotes.py**: Script para consultar y mostrar las citas de un autor específico desde la base de datos. Solicita al usuario el nombre del autor (con la opción de usar un valor predeterminado) y muestra todas las citas asociadas al mismo.


## Esquema de la base de datos
![Esquema de la Base de Datos](./schema.png)

## Requisitos

- Python 3.11+
- Bibliotecas de Python:
  - `requests`
  - `BeautifulSoup4`
  - `sqlite3` (incluida por defecto en Python)

## Instrucciones de ejecución


1. **Configurar entorno virtual**:
   - En macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar scraping**:
   ```bash
   cd src
   python main.py
   ```

4. **Obtener citas por autor**:
   ```bash
   python get_quotes.py
   ```

5. **Desactivar entorno virtual** (opcional):
   ```bash
   deactivate
   ```


## Autor

[Juan De Luca](https://github.com/delucajuan/)