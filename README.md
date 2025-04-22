# Instrucciones para Instalar y Ejecutar Python

Guía para instalar Visual Studio Code (VS Code), Python y ejecutar archivos de Python en tu sistema.

## Instalar Visual Studio Code (VS Code)

1.  **Sitio web de VS Code:**  [https://code.visualstudio.com/](https://code.visualstudio.com/).

2.  **Descargar versión correcta:** La página detectará automáticamente tu sistema operativo (Windows, macOS o Linux). Haz clic en el botón de descarga correspondiente.

3.  **Ejecuta el instalador:** Una vez que la descarga se complete, haz doble clic en el archivo descargado para iniciar el proceso de instalación.

4.  **Sigue las instrucciones:** Lee y acepta el acuerdo de licencia. Sigue los pasos del asistente de instalación. Es recomendable dejar las opciones predeterminadas marcadas, incluyendo la opción de agregar VS Code al PATH para poder ejecutarlo desde la terminal.

5.  **Finalizar la instalación:** Una vez que la instalación se complete, hacer clic en "Finalizar" para abrir VS Code.

## Paso 2: Instalar Python

Necesitas tener Python instalado en tu sistema para poder ejecutar archivos `.py`.

1.  **Ve al sitio web oficial de Python:** Abre tu navegador web y visita [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Descarga la última versión de Python 3:** Haz clic en el botón que dice "Download Python X.Y.Z" (donde X.Y.Z es la última versión). Asegúrate de descargar la versión para tu sistema operativo.
3.  **Ejecuta el instalador:** Una vez que la descarga se complete, haz doble clic en el archivo descargado para iniciar el proceso de instalación.
4.  **¡Importante! Marca la casilla "Add Python X.Y to PATH":** Durante la instalación, asegúrate de marcar la casilla que dice algo como "Add Python 3.x to PATH". Esto permitirá que puedas ejecutar Python desde la línea de comandos.
5.  **Haz clic en "Install Now":** Para una instalación estándar, puedes hacer clic en este botón. Si deseas personalizar la instalación, elige "Customize installation".
6.  **Finaliza la instalación:** Una vez que la instalación se complete, haz clic en "Cerrar". Es posible que necesites reiniciar tu computadora si marcaste la opción de agregar Python al PATH.

## Paso 3: Ejecutar Archivos de Python con VS Code

Ejecutar archivos de Python.

1.  **Abrir VS Code:** Inicia la aplicación Visual Studio Code.
2.  **Abrir la carpeta de tu proyecto (opcional pero recomendado):** Ve a "Archivo" (File) > "Abrir Carpeta" (Open Folder...) y selecciona la carpeta donde guardarás tus archivos de Python. Esto te ayudará a organizar tus proyectos.
3.  **Crea un nuevo archivo de Python:** Ve a "Archivo" (File) > "Nuevo Archivo" (New File) o usa el atajo de teclado `Ctrl+N` (Windows/Linux) o `Cmd+N` (macOS).
4.  **Guarda el archivo:** Ve a "Archivo" (File) > "Guardar como..." (Save As...) o usa el atajo de teclado `Ctrl+S` (Windows/Linux) o `Cmd+S` (macOS). Guarda el archivo con una extensión `.py` (por ejemplo, `mi_script.py`).
5.  **Escribe tu código Python:** Escribe el código Python que deseas ejecutar en el editor. Por ejemplo, puedes copiar y pegar alguno de los ejercicios que te proporcioné anteriormente.
6.  **Ejecuta el archivo:** Hay varias formas de ejecutar tu archivo de Python en VS Code:
    * **Usando el botón "Run Python File" (Play):** En la esquina superior derecha de la ventana del editor, deberías ver un botón con un icono de "Play" (un triángulo). Haz clic en este botón para ejecutar el archivo. La salida del programa se mostrará en el panel de la "Terminal" en la parte inferior de la ventana de VS Code.
    * **Usando la Terminal integrada:**
        * Ve a "Terminal" > "Nueva Terminal" (New Terminal) para abrir una terminal dentro de VS Code.
        * Navega hasta el directorio donde guardaste tu archivo `.py` utilizando el comando `cd` (change directory). Por ejemplo, si guardaste el archivo en una carpeta llamada "python\_ejercicios" en tu escritorio, escribirías `cd Desktop/python_ejercicios` (la sintaxis puede variar ligeramente según tu sistema operativo).
        * Una vez en el directorio correcto, ejecuta el archivo de Python escribiendo `python nombre_del_archivo.py` (reemplaza `nombre_del_archivo.py` con el nombre de tu archivo, por ejemplo, `python mi_script.py`) y presiona Enter. La salida del programa se mostrará en la terminal.

