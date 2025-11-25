import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import sys
from datetime import datetime

def limpiar_pantalla():
    """Limpia la pantalla de forma multiplataforma"""
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    """Muestra el banner de la aplicación"""
    print("")
    print("\033[31m" + r"  __      __      ___.       _________                          .__                   " + "\033[0m")
    print("\033[31m" + r" /  \    /  \ ____\_ |__    /   _____/ ________________  ______ |__| ____    ____     " + "\033[0m")
    print("\033[31m" + r" \   \/\/   // __ \| __ \   \_____  \_/ ___\_  __ \__  \ \____ \|  |/    \  / ___\    " + "\033[0m")
    print("\033[31m" + r"  \        /\  ___/| \_\ \  /        \  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >   " + "\033[0m")
    print("\033[31m" + r"   \__/\  /  \___  >___  / /_______  /\___  >__|  (____  /   __/|__|___|  /\___  /    " + "\033[0m")
    print("\033[31m" + r"        \/       \/    \/          \/     \/           \/|__|           \//_____/     " + "\033[0m")
    print("")

def crear_carpeta(nombre):
    """Crea una carpeta si no existe"""
    if not os.path.exists(nombre):
        os.makedirs(nombre)
        print(f"[✓] Carpeta creada: {nombre}")
    return nombre

def validar_url(url):
    """Valida que la URL tenga un formato correcto"""
    try:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])
    except:
        return False

def obtener_contenido_web(url, timeout=10):
    """Obtiene el contenido HTML de una URL con manejo de errores"""
    try:
        sesion = requests.Session()
        sesion.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        print(f"\n[*] Conectando a: {url}")
        response = sesion.get(url, timeout=timeout)
        response.raise_for_status()
        
        print(f"[✓] Conexión exitosa (Status: {response.status_code})")
        return response
        
    except requests.exceptions.Timeout:
        print(f"[!] Error: Tiempo de espera agotado ({timeout}s)")
        return None
    except requests.exceptions.ConnectionError:
        print("[!] Error: No se pudo conectar al servidor")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"[!] Error HTTP: {e}")
        return None
    except Exception as e:
        print(f"[!] Error inesperado: {e}")
        return None

def pausar():
    """Pausa para que el usuario pueda leer los resultados"""
    input("\n\033[1m[+] Presiona ENTER para continuar...\033[0m")

def scrapear_js_css():
    """Scrapea archivos JS y CSS de una página web"""
    carpeta = crear_carpeta("Salida_JS_CSS")
    
    url = input("\033[1m\n[+] Ingrese la URL: \033[0m").strip()
    
    if not validar_url(url):
        print("[!] URL inválida. Debe incluir http:// o https://")
        pausar()
        return
    
    response = obtener_contenido_web(url)
    if not response:
        pausar()
        return
    
    sopa = BeautifulSoup(response.content, "html.parser")
    
    # Extraer archivos JS
    archivos_js = []
    for script in sopa.find_all("script"):
        src = script.attrs.get("src")
        if src:
            url_completa = urljoin(url, src)
            archivos_js.append(url_completa)
    
    # Extraer archivos CSS
    archivos_css = []
    for link in sopa.find_all("link"):
        href = link.attrs.get("href")
        rel = link.attrs.get("rel", [])
        if href and ("stylesheet" in rel or ".css" in href.lower()):
            url_completa = urljoin(url, href)
            archivos_css.append(url_completa)
    
    # Generar timestamp para los archivos
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Guardar JavaScript
    archivo_js = os.path.join(carpeta, f"javascript_{timestamp}.txt")
    with open(archivo_js, "w", encoding="utf-8") as f:
        f.write(f"URL analizada: {url}\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total de archivos JS: {len(archivos_js)}\n")
        f.write("="*70 + "\n\n")
        for idx, archivo in enumerate(archivos_js, 1):
            f.write(f"{idx}. {archivo}\n")
    
    # Guardar CSS
    archivo_css = os.path.join(carpeta, f"css_{timestamp}.txt")
    with open(archivo_css, "w", encoding="utf-8") as f:
        f.write(f"URL analizada: {url}\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total de archivos CSS: {len(archivos_css)}\n")
        f.write("="*70 + "\n\n")
        for idx, archivo in enumerate(archivos_css, 1):
            f.write(f"{idx}. {archivo}\n")
    
    # Mostrar resumen
    print("\n" + "="*70)
    print("RESUMEN DEL SCRAPING")
    print("="*70)
    print(f"📄 Archivos JavaScript encontrados: {len(archivos_js)}")
    print(f"🎨 Archivos CSS encontrados: {len(archivos_css)}")
    print(f"\n[✓] Resultados guardados en:")
    print(f"    - {archivo_js}")
    print(f"    - {archivo_css}")
    
    # Mostrar primeros 5 archivos de cada tipo
    if archivos_js:
        print(f"\n📄 Primeros archivos JS:")
        for idx, archivo in enumerate(archivos_js[:5], 1):
            print(f"    {idx}. {archivo}")
        if len(archivos_js) > 5:
            print(f"    ... y {len(archivos_js) - 5} más")
    
    if archivos_css:
        print(f"\n🎨 Primeros archivos CSS:")
        for idx, archivo in enumerate(archivos_css[:5], 1):
            print(f"    {idx}. {archivo}")
        if len(archivos_css) > 5:
            print(f"    ... y {len(archivos_css) - 5} más")
    
    pausar()

def verificar_disponibilidad():
    """Verifica disponibilidad de URL y extrae enlaces"""
    carpeta = crear_carpeta("Salida_Disponibilidad")
    
    url = input("\033[1m\n[+] Ingrese la URL: \033[0m").strip()
    
    if not validar_url(url):
        print("[!] URL inválida. Debe incluir http:// o https://")
        pausar()
        return
    
    response = obtener_contenido_web(url)
    if not response:
        pausar()
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extraer título
    title = soup.title.text.strip() if soup.title else "Sin título"
    
    # Extraer meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    descripcion = meta_desc.get("content", "Sin descripción") if meta_desc else "Sin descripción"
    
    # Extraer todos los enlaces
    enlaces_internos = []
    enlaces_externos = []
    enlaces_relativos = []
    
    dominio_base = urlparse(url).netloc
    
    for link in soup.find_all("a"):
        href = link.get("href")
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        
        url_completa = urljoin(url, href)
        texto_link = link.get_text(strip=True)[:50] if link.get_text(strip=True) else "(sin texto)"
        
        dominio_link = urlparse(url_completa).netloc
        
        if href.startswith(("http://", "https://")):
            if dominio_link == dominio_base:
                enlaces_internos.append((url_completa, texto_link))
            else:
                enlaces_externos.append((url_completa, texto_link))
        else:
            enlaces_relativos.append((url_completa, texto_link))
    
    # Eliminar duplicados manteniendo orden
    enlaces_internos = list(dict.fromkeys(enlaces_internos))
    enlaces_externos = list(dict.fromkeys(enlaces_externos))
    enlaces_relativos = list(dict.fromkeys(enlaces_relativos))
    
    # Generar nombre de archivo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_limpio = urlparse(url).netloc.replace(".", "_")
    archivo_salida = os.path.join(carpeta, f"{nombre_limpio}_{timestamp}.txt")
    
    # Guardar resultados
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write("="*70 + "\n")
        f.write("ANÁLISIS DE URL\n")
        f.write("="*70 + "\n\n")
        f.write(f"URL: {url}\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Status Code: {response.status_code}\n")
        f.write(f"Título: {title}\n")
        f.write(f"Descripción: {descripcion}\n\n")
        
        f.write("="*70 + "\n")
        f.write(f"ENLACES INTERNOS ({len(enlaces_internos)})\n")
        f.write("="*70 + "\n")
        for idx, (enlace, texto) in enumerate(enlaces_internos, 1):
            f.write(f"\n{idx}. {enlace}\n")
            f.write(f"   Texto: {texto}\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write(f"ENLACES EXTERNOS ({len(enlaces_externos)})\n")
        f.write("="*70 + "\n")
        for idx, (enlace, texto) in enumerate(enlaces_externos, 1):
            f.write(f"\n{idx}. {enlace}\n")
            f.write(f"   Texto: {texto}\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write(f"ENLACES RELATIVOS ({len(enlaces_relativos)})\n")
        f.write("="*70 + "\n")
        for idx, (enlace, texto) in enumerate(enlaces_relativos, 1):
            f.write(f"\n{idx}. {enlace}\n")
            f.write(f"   Texto: {texto}\n")
    
    # Mostrar resumen en pantalla
    print("\n" + "="*70)
    print("ANÁLISIS COMPLETADO")
    print("="*70)
    print(f"🌐 URL: {url}")
    print(f"✅ Status: {response.status_code}")
    print(f"📄 Título: {title}")
    print(f"📝 Descripción: {descripcion[:100]}...")
    print(f"\n📊 ESTADÍSTICAS:")
    print(f"   🔗 Enlaces internos: {len(enlaces_internos)}")
    print(f"   🌍 Enlaces externos: {len(enlaces_externos)}")
    print(f"   📁 Enlaces relativos: {len(enlaces_relativos)}")
    print(f"   📈 Total de enlaces: {len(enlaces_internos) + len(enlaces_externos) + len(enlaces_relativos)}")
    print(f"\n[✓] Resultados guardados en: {archivo_salida}")
    
    pausar()

def menu_principal():
    """Menú principal de la aplicación"""
    while True:
        limpiar_pantalla()
        banner()
        print("="*70)
        print("MENÚ PRINCIPAL")
        print("="*70)
        print("")
        print("  [1] Scrapear archivos JS y CSS")
        print("  [2] Verificar disponibilidad de URL y extraer enlaces")
        print("  [3] Salir")
        print("")
        
        opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
        
        if opcion == "":
            print("\033[1m\n[!] Por favor ingrese una opción válida.\033[0m")
            pausar()
        elif opcion == "1":
            scrapear_js_css()
        elif opcion == "2":
            verificar_disponibilidad()
        elif opcion == "3":
            limpiar_pantalla()
            print("\n[✓] ¡Gracias por usar Web Scraping Tool! Hasta luego.\n")
            break
        else:
            print("\033[1m[!] Opción no válida.\033[0m")
            pausar()

def main():
    """Función principal"""
    try:
        menu_principal()
    except KeyboardInterrupt:
        limpiar_pantalla()
        print("\n[!] Programa interrumpido por el usuario\n")
        sys.exit(0)

if __name__ == "__main__":
    main()