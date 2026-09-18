import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Mostrar los primeros registros
print(df.head())

# =========================================
# EXPLORACION INICIAL
# =========================================

# Numero de registros
print("\nNumero de registros:")
print(df.shape[0])

# Numero de columnas
print("\nNumero de columnas:")
print(df.shape[1])

# Nombre de las variables
print("\nNombre de las variables:")
print(df.columns)

# Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Valores faltantes
print("\nValores faltantes:")
print(df.isnull().sum())

# Registros duplicados
print("\nRegistros duplicados:")
print(df.duplicated().sum())

# Estadisticas descriptivas
print("\nEstadisticas descriptivas:")
print(df.describe())
# =========================================
# LIMPIEZA Y PREPROCESAMIENTO
# =========================================

# Crear una copia del dataset
df_clean = df.copy()
df_clean = df_clean.drop_duplicates()
df_clean = df_clean.reset_index(drop=True)

# Cambiar nombres de las columnas
df_clean.columns = [
    "gender",
    "race_ethnicity",
    "parental_level_of_education",
    "lunch",
    "test_preparation_course",
    "math_score",
    "reading_score",
    "writing_score"
]

# Mostrar los nuevos nombres
print("\nColumnas despues de la limpieza:")
print(df_clean.columns)
# =========================================
# CREACION DE AVERAGE_SCORE
# =========================================

df_clean["average_score"] = (
    df_clean["math_score"] +
    df_clean["reading_score"] +
    df_clean["writing_score"]
) / 3

print("\nPromedio general de los primeros estudiantes:")
print(df_clean[[
    "math_score",
    "reading_score",
    "writing_score",
    "average_score"
]].head())

# =========================================
# CLASIFICACION DEL RENDIMIENTO
# =========================================

df_clean["performance"] = ""

for i in range(len(df_clean)):

    promedio = df_clean.loc[i, "average_score"]

    if promedio < 60:
        df_clean.loc[i, "performance"] = "Bajo"

    elif promedio < 80:
        df_clean.loc[i, "performance"] = "Medio"

    else:
        df_clean.loc[i, "performance"] = "Alto"

print("\nClasificacion del rendimiento:")
print(df_clean[["average_score", "performance"]].head())

# =========================================
# ANALISIS DE LOS DATOS
# =========================================

# ANALISIS 1
# ¿Cual de las tres areas tiene el promedio mas alto?

print("\nANALISIS 1 - Promedio por materia")

promedio_matematicas = df_clean["math_score"].mean()
promedio_lectura = df_clean["reading_score"].mean()
promedio_escritura = df_clean["writing_score"].mean()

print("Matematicas:", promedio_matematicas)
print("Lectura:", promedio_lectura)
print("Escritura:", promedio_escritura)


# ANALISIS 2
# ¿Los estudiantes que realizaron el curso de preparacion
# presentan mejores resultados?

print("\nANALISIS 2 - Curso de preparacion")

promedio_curso = df_clean.groupby(
    "test_preparation_course"
)["average_score"].mean()

print(promedio_curso)


# ANALISIS 3
# ¿Existen diferencias segun el nivel educativo de los padres?

print("\nANALISIS 3 - Nivel educativo de los padres")

promedio_padres = df_clean.groupby(
    "parental_level_of_education"
)["average_score"].mean()

print(promedio_padres)


# ANALISIS 4
# ¿Que porcentaje de estudiantes tiene rendimiento bajo, medio o alto?

print("\nANALISIS 4 - Porcentaje por rendimiento")

porcentaje_rendimiento = (
    df_clean["performance"].value_counts(normalize=True) * 100
)

print(porcentaje_rendimiento)

# =========================================
# VISUALIZACIONES
# =========================================

# GRAFICA 1 - Promedio por materia

materias = ["Matematicas", "Lectura", "Escritura"]
promedios = [
    df_clean["math_score"].mean(),
    df_clean["reading_score"].mean(),
    df_clean["writing_score"].mean()
]

plt.figure()
plt.bar(materias, promedios)
plt.title("Promedio por materia")
plt.ylabel("Promedio")
plt.tight_layout()
plt.savefig("outputs/resultados/promedio_materias.png")
plt.close()


# GRAFICA 2 - Curso de preparacion

promedio_curso.plot(kind="bar")

plt.title("Promedio segun curso de preparacion")
plt.xlabel("Curso de preparacion")
plt.ylabel("Promedio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/resultados/curso_preparacion.png")
plt.close()


# GRAFICA 3 - Rendimiento academico

df_clean["performance"].value_counts().plot(kind="bar")

plt.title("Clasificacion del rendimiento academico")
plt.xlabel("Rendimiento")
plt.ylabel("Numero de estudiantes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/resultados/rendimiento_academico.png")
plt.close()

# =========================================
# CONCLUSIONES
# =========================================

print("\n=== CONCLUSIONES ===")

promedios_por_area = {
    "Matematicas": promedio_matematicas,
    "Lectura": promedio_lectura,
    "Escritura": promedio_escritura
}
area_mas_alta = max(promedios_por_area, key=promedios_por_area.get)

print("- El area con mejor promedio fue:", area_mas_alta)

diferencia_curso = round(promedio_curso.max() - promedio_curso.min(), 2)
print("- Diferencia de promedio entre quienes tomaron el curso de preparacion y quienes no:", diferencia_curso)

porcentaje_alto = round(porcentaje_rendimiento.get("Alto", 0), 2)
print("- Porcentaje de estudiantes con rendimiento Alto:", porcentaje_alto, "%")