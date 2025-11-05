import pandas as pd

df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';')
print("=== DATASET ORIGINAL ===")
print(f"Total filas: {len(df)}")
print(f"Columnas: {list(df.columns)}")

if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print(f"\nFilas con NaN: {df.isna().any(axis=1).sum()}")
print(f"Duplicados completos: {df.duplicated().sum()}")

# Limpieza básica
text_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.lower().str.strip()

df = df.dropna()
df = df.drop_duplicates()

print(f"\n=== DESPUÉS DE LIMPIEZA BÁSICA ===")
print(f"Total filas: {len(df)}")

print(f"\nDistribución Sexo:")
sexo_counts = df['sexo'].value_counts()
print(sexo_counts)
print(f"Lista: {sexo_counts.to_list()}")

print(f"\nDistribución Tipo de Emprendimiento:")
tipo_counts = df['tipo_de_emprendimiento'].value_counts()
print(tipo_counts)
print(f"Lista: {tipo_counts.to_list()}")

print(f"\n=== OBJETIVOS ===")
print(f"Sexo objetivo: [6617, 3589] -> Total: 10206")
print(f"Tipo objetivo: [5636, 2205, 2201, 164] -> Total: 10206")
print(f"\nDiferencia: {len(df)} - 10206 = {len(df) - 10206} filas")

# Analizar duplicados en diferentes subsets
print(f"\n=== ANÁLISIS DE DUPLICADOS ===")
subsets_test = [
    ['tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'estrato', 'fecha_de_beneficio'],
    ['idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 'línea_credito', 'fecha_de_beneficio'],
    ['tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 'fecha_de_beneficio'],
]

for subset in subsets_test:
    dups = df.duplicated(subset=subset, keep=False).sum()
    print(f"\nDuplicados en {subset[:3]}...: {dups}")
