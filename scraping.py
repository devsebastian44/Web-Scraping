import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# Limpieza compatible con Windows y Linux
os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("")
    print("\33[31m" + r"  __      __      ___.       _________                          .__                   " + "\033[0m")
    print("\33[31m" + r" /  \    /  \ ____\_ |__    /   _____/ ________________  ______ |__| ____    ____     " + "\033[0m")
    print("\33[31m" + r" \   \/\/   // __ \| __ \   \_____  \_/ ___\_  __ \__  \ \____ \|  |/    \  / ___\    " + "\033[0m")
    print("\33[31m" + r"  \        /\  ___/| \_\ \  /        \  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >   " + "\033[0m")
    print("\33[31m" + r"   \__/\  /  \___  >___  / /_______  /\___  >__|  (____  /   __/|__|___|  /\___  /    " + "\033[0m")
    print("\33[31m" + r"        \/       \/    \/          \/     \/           \/|__|           \//_____/     " + "\033[0m")
    print("")


def crear_carpeta(nombre):
    if not os.path.exists(nombre):
        os.makedirs(nombre)
    return nombre


def menu_principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner() 
        print("")
        print("  [1] Scrapear archivos JS y CSS")
        print("  [2] Verificar disponibilidad de URL y extraer enlaces")
        print("  [3] Extraer todos los enlaces de una página web")
        print("  [4] Salir")

        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")

        if opcion == "":
            print("\033[1m\n[+] Por favor ingrese una opción válida.\033[0m")
            continue

        if opcion == "1":
            menu1()
        elif opcion == "2":
            menu2()
        elif opcion == "3":
            menu3()
        elif opcion == "4":
            break
        else:
            print("\033[1m[+] Opción no válida.\033[0m")


def regresar_menu():
    input("\n\033[1m[+] Presiona ENTER para regresar al menú principal...\033[0m")
    os.system("cls" if os.name == "nt" else "clear")
    banner()


def menu1():
    carpeta = crear_carpeta("Salida_JS_CSS")

    while True:
        url = input("\033[1m\n[+] Ingrese la URL: \033[0m")

        try:
            sesion = requests.Session()
            sesion.headers["User-Agent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
            )
            html = sesion.get(url).content
        except Exception as e:
            print(f"Error al conectar: {e}")
            continue

        sopa = BeautifulSoup(html, "html.parser")

        archivos_de_script = []
        archivos_de_css = []

        for script in sopa.find_all("script"):
            if script.attrs.get("src"):
                url_script = urljoin(url, script.attrs.get("src"))
                archivos_de_script.append(url_script)

        for css in sopa.find_all("link"):
            if css.attrs.get("href") and "css" in css.attrs.get("href"):
                url_css = urljoin(url, css.attrs.get("href"))
                archivos_de_css.append(url_css)

        with open(os.path.join(carpeta, "javascript.txt"), "w") as f:
            for archivo_js in archivos_de_script:
                f.write(archivo_js + "\n")

        with open(os.path.join(carpeta, "css.txt"), "w") as f:
            for archivo_css in archivos_de_css:
                f.write(archivo_css + "\n")
        
        print("")
        print("Total de archivos JS:", len(archivos_de_script))
        print("Total de archivos CSS:", len(archivos_de_css))
        print(f"[+] Archivos guardados en: {carpeta}")

        regresar_menu()
        break


def menu2():
    carpeta = crear_carpeta("Salida_Disponibilidad")

    while True:
        url = input("\033[1m\n[+] Ingrese la URL: \033[0m")

        try:
            response = requests.get(url)

            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.text if soup.title else "Sin título"

            links = [link.get("href") for link in soup.find_all("a") if link.get("href")]
            links_text = "\n[+] ".join(links)

            file_name = (
                url.replace("http://", "")
                .replace("https://", "")
                .replace(".", "_")
                .replace("/", "_")
            ) + ".txt"

            ruta_archivo = os.path.join(carpeta, file_name)

            with open(ruta_archivo, "w+") as f:
                f.write(f"Título: {title}\n\nEnlaces:\n[+] {links_text}")

            print("")    
            print(f"Título: {title}")
            print("Enlaces encontrados:")
            print(links_text)
            print(f"[+] Archivo guardado en: {ruta_archivo}")

        except Exception as e:
            print(f"No se pudo acceder: {e}")

        regresar_menu()
        break


def menu3():
    carpeta = crear_carpeta("Salida_Enlaces")

    while True:
        url = input("\033[1m\n[+] Ingrese la URL: \033[0m")

        try:
            response = requests.get(url)
        except:
            print("Error al conectar.")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        links = [link.get('href') for link in soup.find_all('a') if link.get("href")]

        filename = os.path.basename(url).replace("/", "_") + '.txt'
        ruta_archivo = os.path.join(carpeta, filename)

        with open(ruta_archivo, 'w+') as f:
            print("")
            for link in links:
                f.write("[+] " + link + "\n")
                print("[+] " + link)

        print("\n[+] La salida se ha guardado en:", ruta_archivo)

        regresar_menu()
        break


menu_principal()
