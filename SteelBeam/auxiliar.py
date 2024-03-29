import pandas as pd


def table_steel(product):
    path = './tabelas.xlsx'
    return pd.read_excel(path, sheet_name = product)
    

def dados_perfis(product, bitola):
    df = table_steel(product)
    filtro = bitola

    df_select = df.loc[df.iloc[:,0] == filtro]
    listaParam = df_select.iloc[0].tolist()

    return listaParam


def lista_bitolas(product):
    df = table_steel(product)

    df_list = df.iloc[:,0].tolist()

    return df_list


   