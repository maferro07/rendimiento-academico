import pandas as pd

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