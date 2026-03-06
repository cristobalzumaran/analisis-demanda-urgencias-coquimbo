import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# ----------------------------------------
# 1. CARGA Y LIMPIEZA DE DATOS
# ----------------------------------------
def cargar_y_limpiar_datos(path):

    df = pd.read_csv(path)

    # estandarizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # eliminar duplicados
    df = df.drop_duplicates()

    # eliminar registros críticos incompletos
    df = df.dropna(subset=['categoria_riesgo', 'diagnostico_cie10'])

    # separar columnas numéricas y categóricas
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include="object").columns

    # imputar valores faltantes
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    df[cat_cols] = df[cat_cols].fillna("desconocido")

    # limpiar texto
    for col in cat_cols:
        df[col] = df[col].str.strip().str.lower()

    # eliminar outliers usando IQR
    for col in num_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        df = df[
            (df[col] >= q1 - 1.5 * iqr) &
            (df[col] <= q3 + 1.5 * iqr)
        ]

    df = df.reset_index(drop=True)

    print("Datos cargados y limpiados correctamente")

    return df


# ----------------------------------------
# 2. ANÁLISIS DE INDICADORES
# ----------------------------------------
def analizar_indicadores(df):

    resolutividad = df['condicion_egreso'].value_counts(normalize=True)

    print("\nResolutividad del servicio:")
    print(resolutividad)

    return resolutividad


# ----------------------------------------
# 3. MODELO PREDICTIVO
# ----------------------------------------
def proyectar_demanda(df):

    X = df[['mes_num']]
    y = df['total_atenciones']

    modelo = LinearRegression()
    modelo.fit(X, y)

    print("\nModelo de regresión entrenado correctamente")

    return modelo


# ----------------------------------------
# 4. VISUALIZACIÓN
# ----------------------------------------
def graficar_demanda(df):

    demanda_mensual = df.groupby('mes_num')['total_atenciones'].sum()

    plt.figure(figsize=(8,5))
    plt.plot(demanda_mensual.index, demanda_mensual.values, marker='o')
    plt.title("Demanda mensual de urgencias")
    plt.xlabel("Mes")
    plt.ylabel("Total de atenciones")
    plt.grid(True)

    plt.show()


# ----------------------------------------
# 5. PIPELINE PRINCIPAL
# ----------------------------------------
def main():

    path = "data/dataset_sintetico_urgencias.csv"

    df = cargar_y_limpiar_datos(path)

    analizar_indicadores(df)

    modelo = proyectar_demanda(df)

    graficar_demanda(df)


# ejecutar programa
if __name__ == "__main__":
    main()
