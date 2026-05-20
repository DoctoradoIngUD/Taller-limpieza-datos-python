# Taller de Limpieza, Normalización y Calidad de Datos con Python

## Descripción

Repositorio del workshop orientado al desarrollo de procesos de limpieza, transformación, validación y automatización de datos utilizando Python y Pandas.

El proyecto evoluciona desde análisis exploratorio básico hasta construcción de pipelines ETL modulares con métricas de calidad y validaciones empresariales.

---

# Objetivos

Durante el workshop se desarrollan competencias relacionadas con:

- limpieza y transformación de datos
- análisis exploratorio (EDA)
- automatización de procesos ETL
- validación y calidad de datos
- construcción de pipelines analíticos
- arquitectura modular para procesamiento de información

---

# Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | procesamiento principal |
| Pandas | manipulación de datos |
| NumPy | operaciones numéricas |
| Matplotlib | visualización |
| Seaborn | análisis gráfico |
| Jupyter Notebook | entorno interactivo |
| Git & GitHub | control de versiones |

---

# Estructura del proyecto

```text
Taller-limpieza-datos-python/
│
├── data/
│   └── raw/
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── cleaning.py
│   ├── validators.py
│   ├── metrics.py
│   ├── etl_pipeline.py
│   ├── generate_dataset.py
│   └── generate_proyecto_final.py
│
├── requirements.txt
└── README.md
```

---

# Componentes principales

| Archivo | Función |
|---|---|
| cleaning.py | limpieza y transformación |
| validators.py | reglas de validación |
| metrics.py | métricas de calidad |
| etl_pipeline.py | automatización ETL |
| notebooks/ | notebook maestro del workshop |

---

# Contenido del workshop

| Módulo | Tema |
|---|---|
| 0 | Introducción ETL y calidad de datos |
| 1 | Problemas comunes en datasets |
| 2 | Pandas y exploración inicial |
| 3 | Calidad de datos y profiling |
| 4 | Limpieza y transformación |
| 5 | Visualización y análisis exploratorio |
| 6 | Automatización y pipelines ETL |
| 7 | Ingeniería de calidad de datos y pipelines analíticos |

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/DoctoradoIngUD/Taller-limpieza-datos-python.git
```

---

## 2. Ingresar al proyecto

```bash
cd Taller-limpieza-datos-python
```

---

## 3. Crear entorno virtual (opcional)

### Windows

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución del notebook

Iniciar Jupyter:

```bash
jupyter notebook
```

Abrir el notebook ubicado en:

```text
notebooks/
```

---

# Ejecución del pipeline ETL

Desde terminal:

```bash
cd src
```

Ejecutar:

```bash
python etl_pipeline.py
```

---

# Resultados generados

El pipeline exporta automáticamente:

```text
outputs/
│
├── proyecto_final_limpio.csv
└── proyecto_final_limpio.xlsx
```

---

# Conceptos abordados

El workshop integra conceptos relacionados con:

- ETL
- Data Quality
- Data Governance
- Exploratory Data Analysis
- Automatización de procesos
- Validación empresarial
- Arquitectura modular
- Pipelines analíticos

---

# Resultados esperados

Al finalizar el workshop el participante podrá:

- construir procesos ETL básicos
- limpiar y transformar datasets
- automatizar validaciones
- interpretar métricas de calidad
- desarrollar pipelines reproducibles

---

# Licencia

Uso académico y educativo.