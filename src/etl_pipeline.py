# ============================================
# ETL_PIPELINE.PY
# PIPELINE PROFESIONAL DE CALIDAD DE DATOS
# ============================================

# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================

import pandas as pd


# ============================================
# IMPORTACIÓN DE MÓDULOS
# ============================================

from cleaning import limpiar_dataset

from metrics import (
    generar_reporte_calidad,
    calcular_score_calidad
)


# ============================================
# CONFIGURACIÓN DE RUTAS
# ============================================

RUTA_ENTRADA = (
    '../data/raw/proyecto_final.csv'
)

RUTA_SALIDA_CSV = (
    '../outputs/proyecto_final_limpio.csv'
)

RUTA_SALIDA_EXCEL = (
    '../outputs/proyecto_final_limpio.xlsx'
)


# ============================================
# INICIO DEL PIPELINE
# ============================================

print("\n" + "=" * 60)
print("PIPELINE PROFESIONAL DE CALIDAD DE DATOS")
print("=" * 60)


# ============================================
# EXTRACT
# ============================================

print("\n[1/6] EXTRACT")

print("\nCargando dataset...")

df_original = pd.read_csv(
    RUTA_ENTRADA
)

print("Dataset cargado correctamente.")

print("\nDimensiones iniciales:")

print(df_original.shape)


# ============================================
# MÉTRICAS INICIALES
# ============================================

print("\n[2/6] MÉTRICAS INICIALES")

score_inicial = calcular_score_calidad(
    df_original
)

print(
    f"\nScore inicial de calidad: "
    f"{score_inicial}"
)


print("\nReporte inicial:")

generar_reporte_calidad(
    df_original
)


# ============================================
# TRANSFORM
# ============================================

print("\n[3/6] TRANSFORM")

df_limpio = limpiar_dataset(
    df_original
)


# ============================================
# MÉTRICAS FINALES
# ============================================

print("\n[4/6] MÉTRICAS FINALES")

score_final = calcular_score_calidad(
    df_limpio
)

print(
    f"\nScore final de calidad: "
    f"{score_final}"
)


print("\nReporte final:")

generar_reporte_calidad(
    df_limpio
)


# ============================================
# COMPARACIÓN BEFORE VS AFTER
# ============================================

print("\n[5/6] COMPARACIÓN DE RESULTADOS")

print("\nResumen comparativo:")

print(
    f"\nScore inicial: {score_inicial}"
)

print(
    f"Score final: {score_final}"
)

print(
    f"Mejora total: "
    f"{round(score_final - score_inicial, 2)}"
)


print("\nDimensiones:")

print(
    f"Antes: {df_original.shape}"
)

print(
    f"Después: {df_limpio.shape}"
)


print(
    f"\nDuplicados antes: "
    f"{df_original.duplicated().sum()}"
)

print(
    f"Duplicados después: "
    f"{df_limpio.duplicated().sum()}"
)


# ============================================
# LOAD
# ============================================

print("\n[6/6] LOAD")

print("\nExportando resultados...")


# Exportación CSV

df_limpio.to_csv(
    RUTA_SALIDA_CSV,
    index=False
)


# Exportación Excel

df_limpio.to_excel(
    RUTA_SALIDA_EXCEL,
    index=False
)


print("\nArchivos exportados:")

print(
    f"\nCSV: {RUTA_SALIDA_CSV}"
)

print(
    f"Excel: {RUTA_SALIDA_EXCEL}"
)


# ============================================
# FINALIZACIÓN
# ============================================

print("\n" + "=" * 60)
print("PIPELINE FINALIZADO CORRECTAMENTE")
print("=" * 60)
