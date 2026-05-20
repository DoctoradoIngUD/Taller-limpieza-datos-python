# ============================================
# VALIDATORS.PY
# VALIDACIONES DE CALIDAD DE DATOS
# ============================================

# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================

import pandas as pd
import numpy as np
import re
import unicodedata


# ============================================
# NORMALIZACIÓN GENERAL DE TEXTO
# ============================================

def normalizar_texto(texto):

    """
    Limpieza textual avanzada.
    """

    if pd.isnull(texto):
        return np.nan

    texto = str(texto)

    texto = unicodedata.normalize(
        'NFKD',
        texto
    ).encode(
        'ascii',
        'ignore'
    ).decode(
        'utf-8'
    )

    texto = (
        texto
        .strip()
        .lower()
        .title()
    )

    return texto


# ============================================
# VALIDACIÓN DE EMAILS
# ============================================

def validar_email(email):

    """
    Validación empresarial de correos.
    """

    if pd.isnull(email):
        return np.nan

    email = str(email).strip().lower()

    patron = (
        r'^[a-zA-Z0-9._%+-]+'
        r'@[a-zA-Z0-9.-]+'
        r'\.[a-zA-Z]{2,}$'
    )

    if re.match(patron, email):
        return email

    return np.nan


# ============================================
# VALIDACIÓN DE TELÉFONOS
# ============================================

def validar_telefono(telefono):

    """
    Homologación de teléfonos.
    """

    if pd.isnull(telefono):
        return np.nan

    telefono = str(telefono)

    telefono = re.sub(
        r'[^0-9]',
        '',
        telefono
    )

    # Validación Colombia

    if len(telefono) in [7, 10]:
        return telefono

    return np.nan


# ============================================
# VALIDACIÓN DE FECHAS
# ============================================

def validar_fecha(fecha):

    """
    Conversión y estandarización ISO.
    """

    fecha = pd.to_datetime(
        fecha,
        errors='coerce'
    )

    return fecha


# ============================================
# VALIDACIÓN DE PROMEDIOS
# ============================================

def validar_promedio(valor):

    """
    Validación académica.
    """

    valor = pd.to_numeric(
        valor,
        errors='coerce'
    )

    if pd.isnull(valor):
        return np.nan

    if 0 <= valor <= 5:
        return valor

    return np.nan


# ============================================
# VALIDACIÓN DE CRÉDITOS
# ============================================

def validar_creditos(valor):

    """
    Validación académica.
    """

    valor = pd.to_numeric(
        valor,
        errors='coerce'
    )

    if pd.isnull(valor):
        return np.nan

    if 0 <= valor <= 180:
        return valor

    return np.nan


# ============================================
# VALIDACIÓN DE INGRESOS
# ============================================

def validar_ingresos(valor):

    """
    Tratamiento de outliers financieros.
    """

    valor = pd.to_numeric(
        valor,
        errors='coerce'
    )

    if pd.isnull(valor):
        return np.nan

    if 0 <= valor <= 50000000:
        return valor

    return np.nan


# ============================================
# HOMOLOGACIÓN DE CATEGORÍAS
# ============================================

def homologar_categoria(valor):

    """
    Consistencia categórica.
    """

    valor = normalizar_texto(valor)

    if pd.isnull(valor):
        return np.nan

    homologaciones = {

        'Si': 'Si',
        'Sí': 'Si',
        'No': 'No',

        'Virtual': 'Virtual',
        'Presencial': 'Presencial',
        'Hibrida': 'Hibrida'

    }

    return homologaciones.get(
        valor,
        valor
    )