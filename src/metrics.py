# ============================================
# METRICS.PY
# MÉTRICAS DE CALIDAD DE DATOS
# ============================================

# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================

import pandas as pd
import numpy as np


# ============================================
# MÉTRICA DE COMPLETITUD
# ============================================

def calcular_completitud(df):

    """
    Calcula porcentaje de valores no nulos.
    """

    completitud = (
        1 - (
            df.isnull().sum() / len(df)
        )
    ) * 100

    return completitud.round(2)


# ============================================
# MÉTRICA DE DUPLICADOS
# ============================================

def calcular_duplicados(df):

    """
    Calcula registros duplicados.
    """

    duplicados = df.duplicated().sum()

    porcentaje = (
        duplicados / len(df)
    ) * 100

    return {
        'duplicados': duplicados,
        'porcentaje': round(
            porcentaje,
            2
        )
    }


# ============================================
# MÉTRICA DE TIPOS DE DATOS
# ============================================

def validar_tipos(df):

    """
    Retorna tipos del dataset.
    """

    return df.dtypes


# ============================================
# MÉTRICA DE NULOS
# ============================================

def calcular_nulos(df):

    """
    Total y porcentaje de nulos.
    """

    total = df.isnull().sum()

    porcentaje = (
        total / len(df)
    ) * 100

    resultado = pd.DataFrame({
        'total_nulos': total,
        'porcentaje': porcentaje.round(2)
    })

    return resultado


# ============================================
# SCORE GLOBAL DE CALIDAD
# ============================================

def calcular_score_calidad(df):

    """
    Score global de calidad.
    """

    porcentaje_nulos = (
        df.isnull().sum().sum()
        /
        (df.shape[0] * df.shape[1])
    ) * 100

    porcentaje_duplicados = (
        df.duplicated().sum()
        /
        len(df)
    ) * 100

    score = (
        100
        -
        porcentaje_nulos
        -
        porcentaje_duplicados
    )

    score = max(
        score,
        0
    )

    return round(score, 2)


# ============================================
# REPORTE GENERAL
# ============================================

def generar_reporte_calidad(df):

    """
    Genera reporte completo.
    """

    print("\n" + "=" * 60)
    print("REPORTE DE CALIDAD DE DATOS")
    print("=" * 60)


    # ============================================
    # DIMENSIONES
    # ============================================

    print("\nDimensiones:")
    print(df.shape)


    # ============================================
    # COMPLETITUD
    # ============================================

    print("\nCompletitud (%):")

    print(
        calcular_completitud(df)
    )


    # ============================================
    # DUPLICADOS
    # ============================================

    print("\nDuplicados:")

    print(
        calcular_duplicados(df)
    )


    # ============================================
    # NULOS
    # ============================================

    print("\nValores nulos:")

    print(
        calcular_nulos(df)
    )


    # ============================================
    # SCORE GLOBAL
    # ============================================

    print("\nScore global de calidad:")

    print(
        calcular_score_calidad(df)
    )


    print("\n" + "=" * 60)