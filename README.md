# 🕷️ Web Scraping Pro: Audit & Extraction Tool

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Private_Lab-orange?logo=gitlab)
![GitHub](https://img.shields.io/badge/GitHub-Public_Portfolio-black?logo=github)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Certified-brightgreen)

## 🎯 Objetivo Técnico
Herramienta profesional de **Web Scraping** diseñada para la extracción automatizada de activos (JS, CSS) y auditoría de enlaces. Este proyecto implementa una arquitectura **DevSecOps** real con separación estricta entre el entorno de desarrollo privado (GitLab) y el portafolio público (GitHub).

## 🏗️ Arquitectura del Repositorio
La estructura sigue estándares de escalabilidad y seguridad:

- `src/`: Lógica central del scrapers.
- `tests/`: Batería de pruebas unitarias y de integración (Privado).
- `scripts/`: Automatización DevSecOps, incluyendo `publish_public.ps1`.
- `docs/`: Documentación técnica detallada.
- `configs/`: Configuraciones de entorno y parámetros (Privado).
- `data/`: Repositorio local para resultados y datasets (Ignorado en Git).

## 🔒 Estrategia DevSecOps: GitLab ➔ GitHub
Para garantizar la seguridad y el profesionalismo del portafolio, se utiliza un flujo de sincronización sanitizada:

1. **GitLab (Source of Truth):** Contiene el código completo, CI/CD interno, tests, y configuraciones sensibles.
2. **Sanitización Automática:** El script `publish_public.ps1` automatiza la limpieza antes de publicar.
3. **GitHub (Public Mirror):** Versión lista para producción/portafolio, libre de componentes internos, tests de laboratorio o archivos sensibles.

### ¿Qué se sanitiza?
- Se eliminan carpetas de `tests/` y `configs/`.
- Se remueven scripts de automatización privada.
- Se limpia el CI/CD interno.
- Se excluyen logs y datos temporales.


> [!IMPORTANT]
> El repositorio completo con todo el código funcional (tests, src, binarios construíbles) está disponible operativamente en **GitLab** para su análisis y ejecución integral.

https://gitlab.com/group-data-ia-lab/Web-Scraping.git


## ⚙️ Uso Profesional
### Requisitos
- Python 3.9+
- Dependencias: `requests`, `beautifulsoup4`

### Ejecución
```bash
python src/scraping.py
```

### Publicación Segura (DevSecOps)
Para actualizar el portafolio público desde el entorno de laboratorio:
```powershell
./scripts/publish_public.ps1
```

## ⚠️ Advertencia Ética
Este software se entrega con fines educativos y de auditoría autorizada. El uso de esta herramienta sobre sitios de terceros debe respetar siempre los términos de servicio y el archivo `robots.txt`.