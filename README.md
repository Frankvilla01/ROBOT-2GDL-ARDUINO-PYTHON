# 🤖 Sistema de Control e Interfaz para Robot de 2 Grados de Libertad (2 GDL)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-C%2B%2B-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Completado-brightgreen?style=for-the-badge)
![Area](https://img.shields.io/badge/Área-Mecatrónica%20%26%20Control-orange?style=for-the-badge)

Este repositorio contiene la arquitectura de software e integración de hardware para un **manipulador robótico de 2 Grados de Libertad (2 GDL) articulado**. El sistema combina el procesamiento matemático, cálculo cinemático y la interfaz de usuario desarrollada en **Python**, con el control en tiempo real de los actuadores implementado en un microcontrolador **Arduino**.

---

## 📐 Arquitectura del Sistema

El flujo de trabajo se divide en dos capas principales interconectadas por comunicación serial (UART):

1. **Capa Superior (Python - Master):**
   * **Cinemática & Algoritmos:** Cálculo de posiciones articulares y trayectoria del manipulador.
   * **Validación & Excepciones:** Control de límites físicos, singularidades y filtrado de datos antes de la transmisión.
   * **Estructura de Datos:** Organización modular de coordenadas, ángulos y paquetes de control.

2. **Capa Embebida (Arduino - Slave):**
   * **Recepción Serial:** Parser de comandos en formato binario/cadena para minimizar latencia.
   * **Control de Actuadores:** Generación de señales PWM para posicionamiento directo de servomotores/motores en las articulaciones ($\theta_1, \theta_2$).

---

## 🗂️ Estructura del Repositorio

```text
ROBOT-2GDL-ARDUINO-PYTHON/
│
├── 📁 ROBOT_2GDL/                      # Proyecto / Diagramas del brazo robótico
│
├── ⚡ ROBOT_2GDL.ino                    # Firmware Arduino (Control PWM, lectura Serial)
│
├── 🐍 CODIGO-FINAL.py                   # Script principal de ejecución e interfaz Python
│
├── 🧩 estructura.py                    # Módulo de clases, estructuras de datos y modelo cinemático
│
└── ⚠️ excepciones.py                   # Manejo de errores de transmisión serial y límites angulares
