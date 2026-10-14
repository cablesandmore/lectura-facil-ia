Descripción del Proyecto

Lectura Fácil IA es una aplicación web desarrollada utilizando Python, Streamlit y Google Gemini.

Objetivo

Transformar textos administrativos complejos en versiones más claras y fáciles de entender para personas sin conocimientos legales o administrativos.

Esta aplicación permite al usuario introducir un texto burocrático y obtener automáticamente una versión simplificada que mantiene el significado original, pero utiliza un lenguaje más accesible.

Problema Identificado

Muchas personas tienen dificultades para comprender documentos administrativos debido al uso de lenguaje técnico, terminología legal, frases extensas y estructuras burocráticas complejas.

Esta situación puede provocar:

1. Dificultad para entender trámites y procedimientos.
2. Errores al completar solicitudes o formularios.
3. Dependencia de otras personas para interpretar la información.
4. Pérdida de tiempo en la gestión de documentos.

Solución Propuesta

La aplicación Lectura Fácil IA. Esta permite que cualquier usuario pueda:

a. Copiar y pegar un texto administrativo.
b. Pulsar el botón "Simplificar".
c. btener una versión más sencilla y comprensible del contenido.

Para lograrlo, la aplicación utiliza el modelo Gemini 3.8 Flash de Google.

Usuario Objetivo

La solución está orientada a:

a. Ciudadanos que realizan trámites administrativos.
b. ersonas mayores.
c. Estudiantes.
d. Usuarios sin conocimientos jurídicos.
e. Organizaciones interesadas en mejorar la accesibilidad de sus comunicaciones.


Tecnologías Utilizadas

Las tecnologías utilizadas durante el desarrollo del proyecto son:

1. Python
2. Streamlit
3. Google Gemini API
4. Python Dotenv
5. Git
6. GitHub
7. Streamlit Community Cloud

Arquitectura de la Solución

El flujo general de funcionamiento es el siguiente:

Usuario → Texto administrativo → Streamlit → Gemini 3.8 Flash → Texto simplificado → Usuario

Aplicación Desplegada

URL pública de la aplicación:

https://lectura-facil-ia-t87pa5lslxyj2kgktm7nih.streamlit.app/

Repositorio GitHub:

https://github.com/cablesandmore/lectura-facil-ia

Estructura del Proyecto

El proyecto se encuentra organizado de la siguiente manera:

app.py
requirements.txt
README.md
carpeta capturas
carpeta docs
carpeta notebooks
Configuración Local

Para ejecutar la aplicación localmente es necesario:

Clonar el repositorio.
Crear un entorno virtual de Python.
Instalar las dependencias del archivo requirements.txt.
Crear un archivo .env con la clave de Gemini.
Ejecutar Streamlit.
Configuración de Gemini

La aplicación utiliza una clave API almacenada mediante variables de entorno.

Archivo:

.env

Contenido:

GEMINI_API_KEY="TU_API_KEY"

La clave nunca debe almacenarse directamente dentro del código fuente ni publicarse en GitHub.

Ejemplo de Uso:

"De conformidad con la normativa vigente, la solicitud será evaluada en un plazo máximo de treinta días hábiles a partir de la fecha de recepción."

Resultado Simplificado

"Revisaremos tu solicitud.El proceso puede tardar hasta 30 días laborables.El plazo comienza cuando recibimos tu solicitud."

Funcionalidades Implementadas:

Conversión automática de textos administrativos a lectura fácil.
Integración con Google Gemini.
Interfaz web sencilla e intuitiva.
Gestión segura de credenciales.
Despliegue público en Streamlit Cloud.
Control de versiones mediante Git y GitHub.
Pruebas Realizadas

Se realizaron pruebas utilizando diferentes ejemplos de textos administrativos que incluían:

Terminología legal básica.
Procedimientos administrativos.
Lenguaje institucional.
Frases largas y complejas.
Resultados

Las pruebas demostraron:

Reducción de la complejidad de lectura.
Conservación del significado original.
Mejora de la comprensión para usuarios no técnicos.
Funcionamiento correcto de la integración con Gemini.
Mejoras Futuras

Entre las mejoras que podrían implementarse se encuentran:

Exportación de resultados a PDF.
Soporte para múltiples idiomas.
Historial de conversiones.
Indicador de complejidad textual.
Resumen automático de documentos extensos.
Comparación visual entre texto original y texto simplificado.
Contexto Académico

Este proyecto fue desarrollado como parte del Máster en Inteligencia Artificial.

El objetivo de la actividad consiste en diseñar, desarrollar y desplegar una aplicación funcional basada en Inteligencia Artificial Generativa que resuelva un problema real para usuarios no técnicos utilizando herramientas modernas de desarrollo y despliegue.

Autor

Luis Colón

GitHub: https://github.com/cablesandmore

Aplicación: https://lectura-facil-ia-t87pa5lslxyj2kgktm7nih.streamlit.app/

Fecha: Octubre 2026