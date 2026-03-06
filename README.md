# Análisis Predictivo de Demanda en Urgencias

## Propósito del Proyecto

Este proyecto busca transformar registros de atenciones del sistema en herramientas de análisis y predicción para apoyar la toma de decisiones en la red de urgencias de Atención Primaria de Salud (APS) de la comuna de Coquimbo.

El objetivo es evolucionar desde una gestión reactiva hacia una planificación proactiva basada en datos.

---

## Metodología

El análisis se divide en tres etapas principales:

### 1. ETL y Limpieza de Datos
Procesamiento de registros mediante Python para asegurar la calidad y consistencia de los datos.

### 2. Análisis de Indicadores
Exploración de variables como:

- Horario de atención
- Diagnósticos (CIE-10)
- Indicadores de resolutividad
- Edad del paciente
- Centro de Atención
- Destino de alta
- Fecha
- Sexo
- Estamento

### 3. Modelamiento Predictivo
Se utiliza regresión lineal con **scikit-learn** para proyectar la demanda futura de atenciones.

---

## Tecnologías utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Jupyter Notebook

---

## Privacidad de Datos

El dataset incluido en este repositorio es **sintético** y fue creado únicamente con fines demostrativos.

Representa una simulación de atenciones de urgencia en APS y permite demostrar el flujo de trabajo de análisis de datos:

- Limpieza de datos  
- Análisis de indicadores  
- Modelamiento predictivo  
- Visualización

Este repositorio **no contiene datos reales de pacientes**.
