"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd  
    import os
    
    df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';')
    
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)
    
    text_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']
    
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip()
    
    df = df.dropna()
    
    df = df.drop_duplicates()
    
    df = df.sort_values(['sexo', 'tipo_de_emprendimiento', 'monto_del_credito', 'fecha_de_beneficio'])
    
    df = df.drop_duplicates(
        subset=['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'estrato', 'fecha_de_beneficio'],
        keep='first'
    )
    
    df = df.drop_duplicates(
        subset=['tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 'fecha_de_beneficio'],
        keep='first'
    )
    
    df = df.drop_duplicates(
        subset=['idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 'línea_credito', 'fecha_de_beneficio'],
        keep='first'
    )
    
    os.makedirs('files/output', exist_ok=True)
    
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)
    
    return None
