# Analisis del rendimiento academico

## Descripcion

Este proyecto realiza un analisis exploratorio del rendimiento academico de estudiantes utilizando Python.

Se analizan las calificaciones obtenidas en matematicas, lectura y escritura, asi como algunas caracteristicas relacionadas con los estudiantes.

## Dataset

Nombre del dataset: Students Performance in Exams
Fuente: Kaggle
Archivo utilizado: StudentsPerformance.csv
El dataset contiene informacion sobre 1000 estudiantes y 8 variables.

## Objetivo

El objetivo del proyecto es analizar el rendimiento academico de los estudiantes e identificar patrones relacionados con sus resultados.

## Requisitos

Para ejecutar este proyecto se necesita:

- Python
- Las dependencias incluidas en requirements.txt

## Instalacion

Clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Entrar a la carpeta:

cd rendimiento-academico

Crear el entorno virtual:

python -m venv .venv

Activar el entorno virtual:

.venv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt

## Ejecucion

Para ejecutar el proyecto:

python src/analysis.py

## Analisis realizados

1. Comparacion del promedio de matematicas, lectura y escritura.
2. Comparacion entre estudiantes que completaron el curso de preparacion y quienes no lo realizaron.
3. Analisis segun el nivel educativo de los padres.
4. Porcentaje de estudiantes con rendimiento bajo, medio y alto.

## Clasificacion del rendimiento

Se creo average_score utilizando el promedio de matematicas, lectura y escritura.

- Bajo: promedio menor a 60.
- Medio: promedio de 60 a menos de 80.
- Alto: promedio igual o mayor a 80.

## Resultados

Lectura obtuvo el promedio mas alto con 69.17 puntos, seguida de escritura con 68.05 y matematicas con 66.09.

Los estudiantes que completaron el curso de preparacion obtuvieron un promedio de 72.67, mientras que quienes no lo completaron obtuvieron 65.04.

El promedio mas alto segun el nivel educativo de los padres fue master's degree con 73.60 y el mas bajo fue high school con 63.10.

En la clasificacion del rendimiento:

- 51.7% obtuvo rendimiento medio.
- 28.5% obtuvo rendimiento bajo.
- 19.8% obtuvo rendimiento alto.

## Visualizaciones

El proyecto genera tres graficas que se guardan en la carpeta outputs/resultados.

## Conclusiones

Los resultados muestran que lectura presenta el promedio general mas alto de las tres materias.
Tambien se observa que los estudiantes que completaron el curso de preparacion presentan un promedio mayor que quienes no lo realizaron
Finalmente, la mayor parte de los estudiantes se encuentra en la categoria de rendimiento medio.