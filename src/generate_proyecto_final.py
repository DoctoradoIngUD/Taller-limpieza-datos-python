
# ============================================
# GENERADOR DE DATASET FINAL
# ============================================

import pandas as pd
import numpy as np
import random


# ============================================
# CONFIGURACIÓN
# ============================================

random.seed(42)
np.random.seed(42)


# ============================================
# CATÁLOGOS
# ============================================

nombres = [
    'Juan',
    'Maria',
    'Carlos',
    'Ana',
    'Pedro',
    'Luisa',
    'Andres',
    'Camila',
    'Jorge',
    'Valentina'
]

apellidos = [
    'Gomez',
    'Rodriguez',
    'Lopez',
    'Martinez',
    'Garcia',
    'Hernandez',
    'Castro',
    'Torres'
]

ciudades = [
    'Bogotá',
    'bogota',
    'BOGOTA',
    'Medellín',
    'medellin',
    'Cali',
    'Barranquilla',
    ' Bucaramanga '
]

programas = [
    'Ingeniería',
    'ingenieria',
    'INGENIERIA',
    'Matemáticas',
    'Fisica',
    'fisica',
    'Doctorado'
]

modalidades = [
    'Virtual',
    'Presencial',
    'Hibrida',
    'virtual',
    'PRESENCIAL'
]

estados = [
    'Aprobado',
    'Pendiente',
    'Rechazado',
    'En proceso'
]

becas = [
    'Sí',
    'No',
    'si',
    'NO'
]


# ============================================
# GENERACIÓN DE REGISTROS
# ============================================

registros = []

for i in range(500):

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)

    edad = random.choice([
        random.randint(16, 60),
        'treinta',
        'cincuenta',
        None,
        120
    ])

    ciudad = random.choice(ciudades)

    promedio = random.choice([
        round(random.uniform(2.0, 5.0), 2),
        'cuatro',
        None
    ])

    correo = random.choice([
        f'{nombre.lower()}.{apellido.lower()}@mail.com',
        f'{nombre.lower()}@gmail',
        'correo_invalido',
        None
    ])

    telefono = random.choice([
        '3001234567',
        '(601)1234567',
        '+57 3109876543',
        'abc123',
        None
    ])

    estado = random.choice(estados)

    programa = random.choice(programas)

    modalidad = random.choice(modalidades)

    beca = random.choice(becas)

    creditos = random.choice([
        random.randint(0, 120),
        -5,
        300,
        None
    ])

    ingresos = random.choice([
        random.randint(1000000, 10000000),
        999999999,
        None
    ])

    fecha = random.choice([
        '2025-01-15',
        '15/02/2025',
        '03-20-2025',
        '2025/04/01',
        None
    ])

    registros.append({
        'id_estudiante': i,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'ciudad': ciudad,
        'correo': correo,
        'telefono': telefono,
        'promedio': promedio,
        'estado_solicitud': estado,
        'fecha_registro': fecha,
        'programa': programa,
        'modalidad': modalidad,
        'creditos_aprobados': creditos,
        'beca': beca,
        'ingresos': ingresos
    })


# ============================================
# DATAFRAME
# ============================================

df = pd.DataFrame(registros)


# ============================================
# CREAR DUPLICADOS
# ============================================

duplicados = df.sample(
    20,
    random_state=42
)

df = pd.concat(
    [df, duplicados],
    ignore_index=True
)


# ============================================
# GUARDAR CSV
# ============================================

df.to_csv(
    '../data/raw/proyecto_final.csv',
    index=False
)


# ============================================
# RESULTADO
# ============================================

print('Dataset generado correctamente.')

print('\nDimensiones:')
print(df.shape)

print('\nColumnas:')
print(df.columns.tolist())