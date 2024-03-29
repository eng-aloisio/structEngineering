import pandas as pd

def table_steel(product):
    path = './tabelas.xlsx'
    return pd.read_excel(path, sheet_name = product)
    

def profile_data(product, profile):
    df = table_steel(product)
    filter = profile

    df_select = df.loc[df.iloc[:,0] == filter]
    param_list = df_select.iloc[0].tolist()

    return param_list


def lista_bitolas(product):
    df = table_steel(product)

    df_list = df.iloc[:,0].tolist()

    return df_list


   