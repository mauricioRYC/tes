import os
import subprocess

# Ruta local donde tienes el archivo MSI de Squid
local_squid_msi = os.path.join(
    os.getcwd(), "squid.msi"
)  # Asegúrate de que el archivo MSI esté en tu proyecto

# Ruta de instalación de Squid en Windows (puedes especificarla si es necesaria)
install_path = "C:\\Squid"


def install_squid_msi():
    print("Instalando Squid desde archivo MSI...")

    # Verifica si el archivo existe
    if not os.path.exists(local_squid_msi):
        print(f"El archivo {local_squid_msi} no se encuentra.")
        return

    # Ejecuta el comando msiexec para instalar Squid MSI
    install_command = (
        f'msiexec /i "{local_squid_msi}" /quiet INSTALLDIR="{install_path}"'
    )
    result = subprocess.run(install_command, shell=True)

    if result.returncode == 0:
        print("Squid instalado exitosamente.")
    else:
        print(
            f"Error durante la instalación de Squid. Código de salida: {result.returncode}"
        )


def configure_squid():
    print("Configurando Squid...")
    squid_conf = os.path.join(install_path, "etc", "squid.conf")

    # Cambiar configuración de Squid (esto es solo un ejemplo básico)
    with open(squid_conf, "w") as f:
        f.write("http_port 3128\n")
        f.write("acl all src all\n")
        f.write("http_access allow all\n")

    print("Configuración completada.")


def start_squid():
    print("Iniciando Squid...")
    squid_exe = os.path.join(install_path, "sbin", "squid.exe")

    # Iniciar el servicio de Squid
    result = subprocess.run([squid_exe, "-N", "-d1"])

    if result.returncode == 0:
        print("Squid iniciado exitosamente.")
    else:
        print(f"Error al iniciar Squid. Código de salida: {result.returncode}")


def open_firewall_port():
    print("Abriendo el puerto 3128 en el Firewall de Windows...")
    subprocess.run(
        'netsh advfirewall firewall add rule name="Allow Squid" dir=in action=allow protocol=TCP localport=3128'
    )
    print("Puerto 3128 abierto en el Firewall.")


if __name__ == "__main__":
    install_squid_msi()
    configure_squid()
    start_squid()
    open_firewall_port()
