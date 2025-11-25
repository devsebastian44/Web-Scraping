import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

os.system("clear")

print("")
print("\33[31m  __      __      ___.       _________                          .__                   \033[0m")           
print("\33[31m /  \    /  \ ____\_ |__    /   _____/ ________________  ______ |__| ____    ____     \033[0m")
print("\33[31m \   \/\/   // __ \| __ \   \_____  \_/ ___\_  __ \__  \ \____ \|  |/    \  / ___\    \033[0m")
print("\33[31m  \        /\  ___/| \_\ \  /        \  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >   \033[0m")
print("\33[31m   \__/\  /  \___  >___  / /_______  /\___  >__|  (____  /   __/|__|___|  /\___  /    \033[0m")
print("\33[31m        \/       \/    \/          \/     \/           \/|__|           \//_____/     \033[0m")
print("")


def menu_principal():
    while True:
        print("  [1] Metodo 1")
        print("  [2] Metodo 2")
        print("  [3] Metodo 3")
        print("  [4] Salir")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")

        if opcion == "":
            print("\033[1m\n[+] Por favor ingrese una opción: \033[0m")
        elif opcion == "1":
            menu1()
        elif opcion == "2":
            menu2()
        elif opcion == "3":
            menu3()
        elif opcion == "4":
            break


def menu1():
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

        # Scripts
        for script in sopa.find_all("script"):
            if script.attrs.get("src"):
                url_script = urljoin(url, script.attrs.get("src"))
                archivos_de_script.append(url_script)

        # CSS
        for css in sopa.find_all("link"):
            if css.attrs.get("href") and "css" in css.attrs.get("href"):
                url_css = urljoin(url, css.attrs.get("href"))
                archivos_de_css.append(url_css)

        # Guardar archivos
        with open("javascript.txt", "w") as f:
            for archivo_js in archivos_de_script:
                f.write(archivo_js + "\n")

        with open("css.txt", "w") as f:
            for archivo_css in archivos_de_css:
                f.write(archivo_css + "\n")

        print("Total de archivos JS:", len(archivos_de_script))
        print("Total de archivos CSS:", len(archivos_de_css))


def menu2():
    while True:
        url = input("Ingrese la URL: ")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"La URL {url} está disponible.")
            else:
                print(f"La URL {url} no está disponible. Código HTTP: {response.status_code}")

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

            with open(file_name, "w+") as f:
                f.write(f"Título: {title}\n\nEnlaces:\n[+] {links_text}")

            print(f"Título: {title}")
            print("Enlaces encontrados:")
            print(links_text)

        except Exception as e:
            print(f"No se pudo acceder a la URL {url}: {e}")


def menu3():
    while True:
        url = input("Ingrese la URL: ")

        try:
            response = requests.get(url)
        except:
            print("Error al conectar.")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        links = [link.get('href') for link in soup.find_all('a') if link.get("href")]

        filename = os.path.basename(url).replace("/", "_") + '.txt'

        with open(filename, 'w+') as f:
            for link in links:
                f.write("[+] " + link + "\n")
                print("[+] " + link)

        print("La salida se ha guardado en el archivo", filename)


menu_principal()
