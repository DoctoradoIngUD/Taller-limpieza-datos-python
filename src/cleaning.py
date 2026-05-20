# ============================================
# CLEANING.PY
# ORQUESTADOR DE LIMPIEZA Y CALIDAD
# ============================================

# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================

import pandas as pd
import numpy as np


# ============================================
# IMPORTACIÓN DE VALIDADORES
# ============================================

from validators import (
    normalizar_texto,
    validar_email,
    validar_telefono,
    validar_fecha,
    validar_promedio,
    validar_creditos,
    validar_ingresos,
    homologar_categoria
)


# ============================================
# PIPELINE PRINCIPAL
# ============================================

def limpiar_dataset(df):

    """
    Pipeline profesional de limpieza.
    """

    print("\n" + "=" * 50)
    print("INICIANDO PROCESO DE LIMPIEZA")
    print("=" * 50)


    # ============================================
    # COPIA DE SEGURIDAD
    # ============================================

    df = df.copy()


    # ============================================
    # NORMALIZACIÓN TEXTUAL
    # ============================================

    print("\n[1/8] Normalización textual...")


    columnas_texto = [
        'nombre',
        'apellido',
        'ciudad',
        'programa',
        'modalidad',
        'estado_solicitud'
    ]


    for columna in columnas_texto:

        if columna in df.columns:

            df[columna] = df[columna].apply(
                normalizar_texto
            )


    # ============================================
    # HOMOLOGACIÓN DE CATEGORÍAS
    # ============================================

    print("[2/8] Homologación de categorías...")


    columnas_categoria = [
        'beca',
        'modalidad'
    ]


    for columna in columnas_categoria:

        if columna in df.columns:

            df[columna] = df[columna].apply(
                homologar_categoria
            )


    # ============================================
    # VALIDACIÓN DE EMAILS
    # ============================================

    print("[3/8] Validación de correos...")


    if 'correo' in df.columns:

        df['correo'] = df['correo'].apply(
            validar_email
        )


    # ============================================
    # VALIDACIÓN DE TELÉFONOS
    # ============================================

    print("[4/8] Validación de teléfonos...")


    if 'telefono' in df.columns:

        df['telefono'] = df['telefono'].apply(
            validar_telefono
        )


    # ============================================
    # VALIDACIÓN DE FECHAS
    # ============================================

    print("[5/8] Normalización de fechas...")


    if 'fecha_registro' in df.columns:

        df['fecha_registro'] = df[
            'fecha_registro'
        ].apply(
            validar_fecha
        )


    # ============================================
    # VALIDACIONES NUMÉRICAS
    # ============================================

    print("[6/8] Validaciones numéricas...")


    if 'promedio' in df.columns:

        df['promedio'] = df[
            'promedio'
        ].apply(
            validar_promedio
        )


    if 'creditos_aprobados' in df.columns:

        df['creditos_aprobados'] = df[
            'creditos_aprobados'
        ].apply(
            validar_creditos
        )


    if 'ingresos' in df.columns:

        df['ingresos'] = df[
            'ingresos'
        ].apply(
            validar_ingresos
        )


    # ============================================
    # EDAD
    # ============================================

    print("[7/8] Validación de edades...")


    if 'edad' in df.columns:

        df['edad'] = pd.to_numeric(
            df['edad'],
            errors='coerce'
        )

        df.loc[
            (df['edad'] < 15) |
            (df['edad'] > 90),
            'edad'
        ] = np.nan


    # ============================================
    # IMPUTACIÓN
    # ============================================

    print("[8/8] Imputación y limpieza final...")


    columnas_mediana = [
        'edad',
        'promedio'
    ]


    for columna in columnas_mediana:

        if columna in df.columns:

            mediana = df[columna].median()

            df[columna] = df[
                columna
            ].fillna(
                mediana
            )


    # ============================================
    # ELIMINACIÓN DE DUPLICADOS
    # ============================================

    duplicados_antes = df.duplicated().sum()

    df = df.drop_duplicates()

    duplicados_despues = df.duplicated().sum()


    print(
        f"\nDuplicados eliminados: "
        f"{duplicados_antes - duplicados_despues}"
    )


    # ============================================
    # RESET DE ÍNDICES
    # ============================================

    df = df.reset_index(
        drop=True
    )


    print("\nProceso completado.")

    return df
