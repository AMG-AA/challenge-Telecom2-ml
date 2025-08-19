def detect_irrelevant_columns(df, umbral_nulos=0.5, umbral_unicos=0.95):
    columnas_irrelevantes = []

    if 'customerID' in df.columns:
        columnas_irrelevantes.append('customerID')

    nulos = df.isnull().mean()
    col_nulos = nulos[nulos > umbral_nulos].index.tolist()
    columnas_irrelevantes.extend(col_nulos)

    n_filas = df.shape[0]
    unicos = df.nunique() / n_filas
    col_unicos = unicos[unicos > umbral_unicos].index.tolist()
    columnas_irrelevantes.extend(col_unicos)

    columnas_irrelevantes = list(set(columnas_irrelevantes))
    return columnas_irrelevantes

cols_irrelevantes = detect_irrelevant_columns(df)
print("Columnas irrelevantes detectadas:", cols_irrelevantes)