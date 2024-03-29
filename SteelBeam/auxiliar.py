import pandas as pd

def table_steel(product):
    path = './SteelBeam/tabelas.xlsx'
    return pd.read_excel(path, sheet_name = product)
    

def profile_data(product, section):
    df = table_steel(product)
    filter = section

    df_select = df.loc[df.iloc[:,0] == filter]
    param_list = df_select.iloc[0].tolist()

    return param_list


def profile_list(product):
    df = table_steel(product)

    df_list = df.iloc[:,0].tolist()

    return df_list


