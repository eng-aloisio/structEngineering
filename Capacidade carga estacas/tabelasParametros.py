import pandas as pd


# AOKI E VELOSO


def parametro_aoki_tabela():
    
    coef_K_e_alpha = [
        [1, 1000, 0.014],
        [12, 800, 0.020],
        [123, 700, 0.024],
        [13, 600, 0.030],
        [132, 500, 0.028],
        [2, 400, 0.030],
        [21, 550, 0.022],
        [213, 450, 0.028],
        [23, 230, 0.034],
        [231, 250, 0.030],
        [3, 200, 0.060],
        [31, 350, 0.024],
        [312, 300, 0.028],
        [32, 220, 0.040],
        [321, 330, 0.030]
    ]

    df_parametro_Aoki = pd.DataFrame(coef_K_e_alpha, columns=['Solo', 'K (kPa)', 'Alpha'])

    return df_parametro_Aoki


def fator_correcao_aoki():  
    
    correcao_aoki = [
        ['Escavada', 3, 6],
        ['Raiz',     2, 4],
        ['HCM',      2, 4]
    ]

    df_correcao_aoki = pd.DataFrame(correcao_aoki, columns=['Tipo de estaca', 'F1', 'F2'])

    return df_correcao_aoki



# DECOURT E QUARESMA


def parametro_DC_tabela():
    
    coef_C_DC = [
        [3, 120],
        [31, 120],
        [32, 120],
        [312, 120],
        [321, 120],
        [2, 200],
        [23, 200],
        [231, 200],
        [21, 250],
        [213, 250],
        [1, 400],
        [12, 400],
        [13, 400],
        [123, 400],
        [132, 400]
    ]

    df_parametro_DC = pd.DataFrame(coef_C_DC, columns=['Solo', 'C (kPa)'])
    

    return df_parametro_DC


def fator_alpha_DC():

    coef_Alpha_DC = [
        [  3, 0.85, 0.85, 0.30, 0.85],
        [  3, 0.85, 0.85, 0.30, 0.85],           
        [ 31, 0.60, 0.60, 0.30, 0.60],
        [ 32, 0.60, 0.60, 0.30, 0.60],
        [312, 0.60, 0.60, 0.30, 0.60],
        [321, 0.60, 0.60, 0.30, 0.60],
        [  2, 0.60, 0.60, 0.30, 0.60],           
        [ 21, 0.60, 0.60, 0.30, 0.60],
        [ 23, 0.60, 0.60, 0.30, 0.60],
        [213, 0.60, 0.60, 0.30, 0.60],
        [231, 0.60, 0.60, 0.30, 0.60],
        [ 12, 0.60, 0.60, 0.30, 0.60],
        [ 13, 0.60, 0.60, 0.30, 0.60],
        [123, 0.60, 0.60, 0.30, 0.60],
        [132, 0.60, 0.60, 0.30, 0.60],
        [  1, 0.50, 0.50, 0.30, 0.50]
    ]
        

    df_fator_alpha = pd.DataFrame(coef_Alpha_DC, columns=['Solo', 'Escavada', 'Escavada (b)', 'HCM', 'Raiz'])
    
    return  df_fator_alpha


def fator_beta_DC():

    coef_Beta_DC = [
        [  3, 0.80, 0.90, 1.00, 1.50],            
        [ 31, 0.65, 0.75, 1.00, 1.50],
        [ 32, 0.65, 0.75, 1.00, 1.50],
        [312, 0.65, 0.75, 1.00, 1.50],
        [321, 0.65, 0.75, 1.00, 1.50],
        [  2, 0.65, 0.75, 1.00, 1.50],            
        [ 21, 0.65, 0.75, 1.00, 1.50],
        [ 23, 0.65, 0.75, 1.00, 1.50],
        [213, 0.65, 0.75, 1.00, 1.50],
        [231, 0.65, 0.75, 1.00, 1.50],            
        [ 12, 0.65, 0.75, 1.00, 1.50],
        [ 13, 0.65, 0.75, 1.00, 1.50],
        [123, 0.65, 0.75, 1.00, 1.50],
        [132, 0.65, 0.75, 1.00, 1.50],
        [  1, 0.50, 0.60, 1.00, 1.50]
    ]
        

    df_fator_beta = pd.DataFrame(coef_Beta_DC, columns=['Solo', 'Escavada', 'Escavada (b)', 'HCM', 'Raiz'])
    
    return  df_fator_beta

