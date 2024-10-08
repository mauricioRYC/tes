import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Ruta local donde tienes el archivo MSI de Squid
local_squid_msi = os.path.join(os.getcwd(), "squid.msi")
# Ruta de instalación de Squid en Windows
install_path = "C:\\Squid"

def install_squid_msi():
    print("Instalando Squid desde archivo MSI...")
    if not os.path.exists(local_squid_msi):
        messagebox.showerror("Error", f"El archivo {local_squid_msi} no se encuentra.")
        return

    install_command = (
        f'msiexec /i "{local_squid_msi}" /quiet INSTALLDIR="{install_path}"'
    )
    result = subprocess.run(install_command, shell=True)

    if result.returncode == 0:
        messagebox.showinfo("Éxito", "Squid instalado exitosamente.")
    else:
        messagebox.showerror("Error", f"Error durante la instalación de Squid. Código de salida: {result.returncode}")

def on_install_button_click():
    install_squid_msi()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Instalador de Squid")

# Botón para iniciar la instalación
install_button = tk.Button(root, text="Iniciar Instalación de Squid", command=on_install_button_click)
install_button.pack(pady=20)

# Configura el tamaño de la ventana
root.geometry("300x150")

# Ejecuta la interfaz gráfica
root.mainloop()
