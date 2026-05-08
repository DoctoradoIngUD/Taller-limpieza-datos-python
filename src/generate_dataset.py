import pandas as pd
import numpy as np
import random
from faker import Faker

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

fake = Faker('es_CO')

NUM_REGISTROS = 500

# =========================================================
# VARIABLES CATEGÓRICAS
# =========================================================

programas = [
    'Ingeniería Electrónica',
    'Ingeniería de Sistemas',
    'Ingeniería Industrial',
    'Maestría en Ingeniería',
    'Doctorado en Ingeniería'
]

facultades = [
    'Ingeniería',
    'Tecnológica',
    'Ciencias y Educación'
]

tipos_solicitud = [
    'Certificado de notas',
    'Homologación',
    'Constancia de estudio',
    'Paz y salvo',
    'Cancelación de semestre',
    'Reintegro',
    'Inscripción de materias'
]

estados = [
    'Aprobado',
    'Pendiente',
    'Rechazado',
    'En proceso'
]

modalidades = [
    'Presencial',
    'Virtual',
    'Híbrida'
]

ciudades = [
    'Bogotá',
    'bogota',
    'BOGOTA',
    'Bogota ',
    ' Medellín',
    'Cali',
    'Barranquilla',
    'Bucaramanga'
]

# =========================================================
# GENERACIÓN DE REGISTROS
# =========================================================

registros = []

for i in range(1, NUM_REGISTROS + 1):

    registro = {
        'id_solicitud': i,

        'codigo_estudiante': f"2024{random.randint(10000, 99999)}",

        'documento': random.randint(10000000, 99999999),

        'nombre_estudiante': fake.name(),

        'programa': random.choice(programas),

        'facultad': random.choice(facultades),

        'semestre': random.randint(1, 12),

        'promedio': round(random.uniform(2.0, 5.0), 2),

        'creditos_aprobados': random.randint(0, 180),

        'tipo_solicitud': random.choice(tipos_solicitud),

        'fecha_solicitud': fake.date_between(
            start_date='-2y',
            end_date='today'
        ),

        'estado_solicitud': random.choice(estados),

        'valor_pagado': random.randint(20000, 150000),

        'correo': fake.email(),

        'telefono': fake.phone_number(),

        'ciudad': random.choice(ciudades),

        'modalidad': random.choice(modalidades),

        'edad': random.randint(16, 45),

        'observaciones': fake.sentence()
    }

    registros.append(registro)

# =========================================================
# CREAR DATAFRAME
# =========================================================

df = pd.DataFrame(registros)

# =========================================================
# INSERTAR PROBLEMAS INTENCIONALES
# =========================================================

# ---------------------------------------------------------
# 1. VALORES NULOS
# ---------------------------------------------------------

columnas_nulos = [
    'edad',
    'correo',
    'promedio',
    'telefono'
]

for columna in columnas_nulos:
    indices = df.sample(frac=0.05).index
    df.loc[indices, columna] = np.nan

# ---------------------------------------------------------
# 2. DUPLICADOS
# ---------------------------------------------------------

duplicados = df.sample(10)

df = pd.concat(
    [df, duplicados],
    ignore_index=True
)

# ---------------------------------------------------------
# 3. OUTLIERS
# ---------------------------------------------------------

indices_outliers = df.sample(5).index

df.loc[indices_outliers[0], 'edad'] = 120
df.loc[indices_outliers[1], 'edad'] = 5
df.loc[indices_outliers[2], 'promedio'] = 9.5
df.loc[indices_outliers[3], 'creditos_aprobados'] = 500
df.loc[indices_outliers[4], 'valor_pagado'] = -10000

# ---------------------------------------------------------
# 4. CORREOS INVÁLIDOS
# ---------------------------------------------------------

correos_invalidos = [
    'usuario@gmail',
    'correo.com',
    'estudiante@correo',
    'sin-arroba.com'
]

indices_correos = df.sample(10).index

for idx in indices_correos:
    df.loc[idx, 'correo'] = random.choice(correos_invalidos)

# ---------------------------------------------------------
# 5. FECHAS INCONSISTENTES
# ---------------------------------------------------------

formatos_fecha = [
    '10/02/2024',
    '2024/03/15',
    '15-05-2024'
]

indices_fechas = df.sample(15).index

for idx in indices_fechas:
    df.loc[idx, 'fecha_solicitud'] = random.choice(formatos_fecha)

# ---------------------------------------------------------
# 6. TIPOS DE DATOS INCORRECTOS
# ---------------------------------------------------------

# Convertir columnas a object para permitir mezcla de tipos

columnas_object = [
    'promedio',
    'valor_pagado',
    'edad',
    'creditos_aprobados',
    'semestre'
]

for col in columnas_object:
    df[col] = df[col].astype(object)

indices_tipos = df.sample(5).index

df.loc[indices_tipos[0], 'promedio'] = 'cuatro'
df.loc[indices_tipos[1], 'valor_pagado'] = 'cincuenta mil'
df.loc[indices_tipos[2], 'edad'] = 'desconocida'
df.loc[indices_tipos[3], 'creditos_aprobados'] = 'muchos'
df.loc[indices_tipos[4], 'semestre'] = 'primer'

# ---------------------------------------------------------
# 7. ESPACIOS Y TEXTO INCONSISTENTE
# ---------------------------------------------------------

indices_texto = df.sample(10).index

for idx in indices_texto:
    df.loc[idx, 'ciudad'] = ' Bogotá '

# =========================================================
# EXPORTAR DATASET
# =========================================================

output_path = 'data/raw/solicitudes_robusto.csv'

df.to_csv(
    output_path,
    index=False
)

# =========================================================
# MENSAJES FINALES
# =========================================================

print('\n======================================')
print('DATASET GENERADO CORRECTAMENTE')
print('======================================')

print(f'Registros generados: {len(df)}')

print(f'\nArchivo exportado en:\n{output_path}')

print('\nProblemas incluidos:')
print('- Valores nulos')
print('- Duplicados')
print('- Outliers')
print('- Correos inválidos')
print('- Fechas inconsistentes')
print('- Tipos incorrectos')
print('- Inconsistencias de texto')

print('\n======================================')
