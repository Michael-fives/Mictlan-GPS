## 📖 About This Project

This project was developed independently as a final submission for the Data Structures and Algorithms course, demonstrating proficiency in graph theory and algorithmic problem-solving.
It was fully completed before being committed and uploaded to GitHub.  
All design and implementation decisions were made locally by me.
This repository contains the code for the “Mictlán GPS” system, a graph-based pathfinding prototype for eco-friendly cemeteries.

## 🪦 Mictlán: una alternativa ecológica a los cementerios tradicionales  
### Sistema “Recuérdame”: Impulsado por un GPS bajo el uso de grafos

## 📌 Resumen del proyecto

Se tiene como finalidad proponer un modelo de cementerios ecológicos en los cuales se sustituya la lápida tradicional por un árbol que funcione como sitio de reposo, con el propósito de fomentar la transición hacia una alternativa que no solo permita reducir el impacto forestal en áreas destinadas a la sepultura o en el uso de madera para la fabricación de contenedores de reposo para los individuos fallecidos, sino que también contribuya a la reconstrucción de zonas forestales mediante el sembrado de árboles. Esto se plantea a través de la implementación de un medio respaldado por software, que facilite un entorno social más ameno y agradable para los familiares, con el objetivo de motivar a la sociedad a adoptar este modelo ecológico.
Esto, mediante diversas funcionalidades, siendo el sistema de localización una de ellas.

## 🌳 Contexto ambiental

La deforestación ha generado pérdidas masivas de ecosistemas, agravadas por prácticas como la tala y el uso de madera en la industria funeraria. En México, la situación es crítica con más de 736 mil hectáreas de bosque perdidas. [Leer más](./data/antecedentes.md)

## 💡 Justificación

Ante la creciente crisis ambiental derivada de la deforestación, particularmente agravada por el uso extensivo de terrenos para cementerios convencionales, el desarrollo de tecnologías que promuevan soluciones ecológicas resulta indispensable. En este contexto, el presente proyecto propone una alternativa sustentable mediante la creación de un sistema digital de navegación y gestión para cementerios ecológicos, con base en algoritmos de grafos.

El código desarrollado responde directamente al objetivo general del proyecto: registrar y visualizar la ubicación de los individuos en un cementerio ecológico con una precisión espacial de 40m², fomentando así el uso eficiente del terreno y minimizando la necesidad de expansión territorial que contribuye a la deforestación. Mediante una estructura de grafo, se logra representar de manera digital cada punto del cementerio, permitiendo una organización más eficiente y ecológica del espacio.

El código no es solo una herramienta técnica, sino un componente esencial dentro de una propuesta integral para mitigar el impacto ambiental de la industria funeraria. A través de la digitalización del espacio y la optimización de recursos mediante algoritmos, se promueve una transición hacia prácticas más responsables con los ecosistemas, particularmente en un país como México, donde la deforestación asociada a prácticas humanas sigue en aumento.

## 🎯 Objetivo general

Desarrollar un algoritmo basado en estructuras de grafos que registre y visualice la ubicación de los individuos presentes en un cementerio ecológico, con una precisión de 40m². Este algoritmo será implementado posteriormente en una aplicación de software atractiva e intuitiva, con el propósito de fomentar el uso de esta alternativa ecológica y contribuir a la reducción del impacto ambiental asociado a la deforestación.

## 🎯 Objetivos específicos:

1. Determinar la ruta óptima desde las distintas entradas del cementerio ecológico hasta el yacimiento del familiar, considerando la densidad forestal y las posibles obstrucciones presentes en los caminos.

2. Desarrollar un código capaz de convertir un mapeado en un grafo denso que permita el almacenamiento y la gestión eficiente de la información.

3. Implementar un código dirigido al administrador, que permita modificar la instancia de individuos dentro de cada nodo del grafo.

## 🧠 🧠 Estructura del sistema

El sistema está desarrollado en Python, utilizando únicamente la librería estándar `os` para manejo de rutas.
  
El núcleo del proyecto es una representación de un cementerio ecológico mediante un grafo denso no dirigido.  
Cada nodo almacena información sobre ubicación y ocupación, y el sistema permite:

- Registrar individuos en nodos específicos
- Determinar rutas óptimas desde las entradas hasta un nodo
- Modificar el estado de un nodo mediante un administrador

## 📦 Cómo ejecutar

1. Clona este repositorio.
    git clone https://github.com/Michael-fives/Mictlan-GPS.git
    cd tu-repositorio

2. Accede a la carpeta del codigo fuente.
    cd src

3. Ejecuta el archivo principal.
    python mictlanGPS.py