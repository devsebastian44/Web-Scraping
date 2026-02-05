# 🕷️ Web Scraping Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitLab CI](https://img.shields.io/badge/gitlab-ci-%23181717.svg?logo=gitlab&logoColor=white)](https://about.gitlab.com/)

Herramienta profesional de **Web Scraping** desarrollada en Python para la extracción automatizada de activos (JS, CSS) y el análisis de disponibilidad de enlaces en sitios web.


## 🎯 Objetivo
Este proyecto busca proporcionar una utilidad eficiente y fácil de usar para desarrolladores, analistas de datos y profesionales de ciberseguridad que necesiten auditar o extraer información pública de páginas web de forma estructurada.

## 📂 Estructura del Proyecto
La arquitectura del repositorio sigue estándares profesionales para facilitar la mantenibilidad y escalabilidad:

```text
Web-Scraping/
├── data/           # Repositorio para salidas y datasets generados
├── src/            # Código fuente principal
│   └── scraping.py # Script principal de la aplicación
├── .gitignore      # Definición de archivos excluidos
├── .gitlab-ci.yml  # Configuración de integración continua
├── LICENSE         # Licencia MIT
└── README.md       # Documentación principal
```

## ⚙️ Requisitos
- **Lenguaje:** Python 3.8 o superior
- **Dependencias:**
  - `requests`: Manejo de solicitudes HTTP.
  - `beautifulsoup4`: Análisis de documentos HTML.

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Devsebastian44/Web-Scraping.git
   cd Web-Scraping
   ```

2. **Instalar dependencias:**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Ejecutar la herramienta:**
   ```bash
   python src/scraping.py
   ```

## 🛠️ Funcionalidades
- **Extracción de Activos:** Identifica y lista todos los archivos JavaScript y CSS vinculados a una URL.
- **Auditoría de Enlaces:** Clasifica enlaces en internos, externos y relativos, verificando su disponibilidad.
- **Reportes Automáticos:** Genera archivos de texto estructurados en carpetas dedicadas según el análisis.

## ⚠️ Advertencia Ética
Esta herramienta debe utilizarse exclusivamente con fines educativos, de auditoría autorizada o sobre sitios que permitan el scraping según su archivo `robots.txt`. El autor no se hace responsable del mal uso de este software.

## 📜 Licencia
Este proyecto se distribuye bajo la **Licencia MIT**. Siéntete libre de usarlo, modificarlo y compartirlo.

---
*Desarrollado con ❤️ por [Sebastian](https://github.com/Devsebastian44)*


