 🕷️ Web Scraping — Extractor de Datos y URLs

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Parsing-43B02A?style=flat&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-FF6C37?style=flat&logo=python&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-F7CA18?style=flat&logo=open-source-initiative&logoColor=black)
![Data Science](https://img.shields.io/badge/Área-Data%20Science-8A2BE2?style=flat&logo=databricks&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen?style=flat)

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
pip install requests beautifulsoup4
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

> ⚠️ **Aviso ético:** el uso de esta herramienta sobre sitios sin autorización puede violar sus Términos de Servicio y legislaciones de protección de datos vigentes. El autor no se responsabiliza por usos indebidos.

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura de repositorio distribuida:

| Plataforma | Rol | Contenido |
|---|---|---|
| **GitHub** | Portafolio público | Código fuente, documentación y diagramas |
| **GitLab** | Laboratorio completo | Implementación extendida, tests y configuraciones |

### 🔗 Full Source Code

👉 Código completo e implementación integral disponible en GitLab:
**[https://gitlab.com/group-data-ia-lab/Web-Scraping](https://gitlab.com/group-data-ia-lab/Web-Scraping)**

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
- 🦊 GitLab: [group-data-ia-lab](https://gitlab.com/group-data-ia-lab)

---

<div align="center">
  <sub>🐍 Construido con Python · beautifulsoup4 · requests</sub>
</div>