# 🕷️ Web Scraping — Extractor de Datos y URLs

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Parsing-43B02A?style=flat&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-FF6C37?style=flat&logo=python&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-F7CA18?style=flat&logo=open-source-initiative&logoColor=black)
![Data Science](https://img.shields.io/badge/Área-Data%20Science-8A2BE2?style=flat&logo=databricks&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)

Herramienta de extracción automatizada de datos y recursos desde páginas web estáticas, desarrollada en Python. Permite auditar activos web, recolectar enlaces y procesar el contenido HTML de cualquier sitio objetivo de forma estructurada y reproducible.

---

## 🧠 Overview

Este proyecto implementa un pipeline de web scraping orientado a la recolección de datos públicos desde páginas web. A partir de una URL objetivo, el script realiza peticiones HTTP, parsea el árbol HTML resultante y extrae elementos de interés como hipervínculos, recursos embebidos (JS, CSS) y texto estructurado.

El proyecto está pensado como base modular para tareas de **análisis de datos web**, **auditoría de activos** y **construcción de datasets**, siguiendo buenas prácticas de organización de código con separación clara entre fuentes, documentación y diagramas.

---

## ⚙️ Features

- 🌐 **Peticiones HTTP controladas** — Envío de solicitudes GET con manejo de respuestas y códigos de estado HTTP
- 🧩 **Parseo HTML estructurado** — Navegación del árbol DOM mediante BeautifulSoup4 para extracción precisa de elementos
- 🔗 **Recolección de URLs** — Extracción de todos los hipervínculos (`<a href>`) presentes en la página objetivo
- 📦 **Auditoría de activos** — Detección de recursos embebidos: archivos `.js`, `.css` e imágenes referenciadas
- 💾 **Almacenamiento local de resultados** — Los datos extraídos se guardan en el directorio `data/` (excluido del repositorio)
- 📐 **Diagramas de arquitectura** — Carpeta `diagrams/` con visualizaciones del flujo del sistema
- 📄 **Documentación técnica** — Carpeta `docs/` con especificaciones y guías de uso detalladas

---

## 🛠️ Tech Stack

| Componente | Tecnología | Descripción |
|---|---|---|
| Lenguaje | **Python 3.9+** | Lenguaje principal del proyecto |
| HTTP Client | **requests** | Realización y gestión de peticiones web |
| HTML Parser | **beautifulsoup4** | Parseo y navegación del árbol DOM |
| Parser Backend | **html.parser** | Parser nativo de Python, sin dependencias externas |
| Control de versiones | **Git** | Gestión del historial y ramas del proyecto |

---

## 📦 Installation

### Requisitos previos

- Python **3.9** o superior instalado
- `pip` disponible en el entorno

### Pasos de instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/devsebastian44/Web-Scraping.git

# 2. Ingresar al directorio del proyecto
cd Web-Scraping

# 3. Crear un entorno virtual (recomendado)
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Usage

### Ejecución del script principal

```bash
python src/scraping.py
```

### Flujo de ejecución esperado

```
[*] URL objetivo: https://ejemplo.com
[*] Enviando solicitud HTTP...
[+] Código de estado: 200 OK
[+] Parseando contenido HTML...
[+] URLs encontradas    : 42
[+] Recursos JS         : 8
[+] Recursos CSS        : 4
[*] Resultados almacenados en: data/output.json
```

### Personalización del objetivo

Edita la variable de URL al inicio de `src/scraping.py`:

```python
TARGET_URL = "https://tu-sitio-objetivo.com"
```

---

## 🧪 Testing

El proyecto incluye pruebas automatizadas locales que utilizan **mocks** para simular respuestas HTTP, lo que significa que puedes ejecutar todas las pruebas sin necesidad de conexión a internet ni afectar servidores reales.

Para ejecutar las pruebas:

```bash
# Ejecutar todas las pruebas con pytest
pytest tests/

# O utilizar el módulo unittest integrado de Python
python -m unittest discover tests/
```

---

## 🤝 Contributing

¡Las contribuciones son bienvenidas! Para colaborar en este proyecto:

1. Realiza un **Fork** del repositorio.
2. Clona tu fork localmente: `git clone https://github.com/TU_USUARIO/Web-Scraping.git`
3. Crea una rama para tu feature o bugfix: `git checkout -b feature/nueva-funcionalidad`
4. Realiza tus cambios asegurándote de no incluir credenciales ni endpoints sensibles.
5. Ejecuta las pruebas locales (`pytest tests/`) y asegúrate de que pasen correctamente.
6. Haz commit de tus cambios utilizando **Conventional Commits** (ej. `feat: añade soporte para exportar a CSV`).
7. Sube tus cambios a tu fork: `git push origin feature/nueva-funcionalidad`
8. Abre un **Pull Request** hacia la rama `main` del repositorio original. Nuestro pipeline de CI/CD validará automáticamente tus cambios.

---

## 📁 Project Structure

```
Web-Scraping/
│
├── src/                  # Código fuente principal
│   └── scraping.py       # Script central de extracción y parseo
│
├── docs/                 # Documentación técnica del proyecto
│
├── diagrams/             # Diagramas de arquitectura y flujo de datos
│
├── data/                 # Resultados generados (excluido de Git)
│
├── .gitignore            # Exclusiones del repositorio
├── LICENSE               # Licencia MIT
└── README.md             # Este archivo
```

> Los resultados de ejecución se almacenan localmente en `data/` y no forman parte del historial de Git, garantizando que datos sensibles o datasets privados no sean expuestos accidentalmente.

---

## 🔐 Security

- **Uso responsable obligatorio:** esta herramienta debe utilizarse únicamente sobre sitios web propios o con autorización expresa del propietario del sitio.
- **Respeto a `robots.txt`:** se recomienda verificar y respetar siempre el archivo `robots.txt` del sitio antes de ejecutar cualquier extracción.
- **Sin almacenamiento en el repositorio:** el directorio `data/` está incluido en `.gitignore` para evitar la exposición accidental de datos extraídos.
- **Sin credenciales en el código:** el script no gestiona ni almacena tokens, cookies de sesión ni credenciales de ningún tipo en el código fuente.

> ⚠️ **Aviso ético / Ethical Notice:** This project is for educational and ethical cybersecurity purposes only. El uso de esta herramienta sobre sitios sin autorización puede violar sus Términos de Servicio y legislaciones de protección de datos vigentes. El autor no se responsabiliza por usos indebidos.

---

## 🚀 Roadmap

- [ ] Soporte para argumentos de línea de comandos con `argparse` (URL, formato de salida, verbosidad)
- [ ] Exportación de resultados en múltiples formatos: `JSON`, `CSV`, `Excel`
- [ ] Soporte para sitios dinámicos (JavaScript rendering) mediante integración con **Playwright** o **Selenium**
- [ ] Implementación de manejo automático de `robots.txt` y `rate limiting` configurable
- [ ] Módulo de visualización de resultados con `pandas` y `matplotlib`
- [ ] Containerización con **Docker** para ejecuciones reproducibles y portables
- [ ] Tests unitarios y de integración con `pytest`

---

## 📄 License

Este proyecto está distribuido bajo la licencia **MIT**.
Consulta el archivo [`LICENSE`](./LICENSE) para ver los términos completos.

---

## 👨‍💻 Author

**Sebastian Zhunaula**
Desarrollador de software especializado en automatización de datos y scripting Python.

- 🐙 GitHub: [@devsebastian44](https://github.com/devsebastian44)

---

<div align="center">
  <sub>🐍 Construido con Python · beautifulsoup4 · requests</sub>
</div>