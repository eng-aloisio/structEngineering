from tabelasParametros import parametro_DC_tabela, fator_alpha_DC, fator_beta_DC
import math
import pandas as pd


def searchParamDc(tipoSolo):

    df = parametro_DC_tabela()
    df2 = df.loc[df['Solo'] == tipoSolo]
    lista_C = df2['C (kPa)'].tolist()

    lista_param_DC = [lista_C[0]]

    return lista_param_DC


def searchCorrAlphaDc(tipoSolo, tipoEstaca):

    df = fator_alpha_DC()
    df2 = df.loc[df['Solo'] == tipoSolo]
    
    lista_val_alpha = df2[tipoEstaca].tolist()
    
    return lista_val_alpha


def searchCorrBetaDc(tipoSolo, tipoEstaca):

    df = fator_beta_DC()
    df2 = df.loc[df['Solo'] == tipoSolo]

    lista_valor_beta = df2[tipoEstaca].tolist()

    return lista_valor_beta


def calc_rp(tipoSolo, n1, n2, n3):

    valor_C = searchParamDc(tipoSolo)[0]
    valor_np = (n1 + n2 + n3) / 3

    rp = valor_C * valor_np

    return rp


def valores_rp(listaTipoSolo, listaNspt):

    listaNspt.append(listaNspt[-1])
    listaNspt.insert(0, listaNspt[0])

    lista_val_rp = []
    
    for i in range(len(listaTipoSolo)):
        lista_val_rp.append(calc_rp(listaTipoSolo[i], listaNspt[i], listaNspt[i + 1], listaNspt[i + 2]))

    listaNspt.pop()
    listaNspt.pop(0)
    

    lista_val_rp.pop(0)
    lista_val_rp.append(lista_val_rp[-1])

    return lista_val_rp
    

def prop_geom_estacas(diametro):

    perimetro_estaca = diametro * math.pi
    area_estaca = pow(diametro, 2) * math.pi / 4

    resultados_prop_geom = [diametro, perimetro_estaca, area_estaca]

    return resultados_prop_geom


def valores_C(listaTipoSolo):

    lista_val_C = []
    for tipo_solo in listaTipoSolo:
        lista_val_C.append(searchParamDc(tipo_solo)[0])

    return lista_val_C


def valoresRp(listaTipoSolo, listaNspt, tipoEstaca, diametroEstaca):

    areaEstaca = prop_geom_estacas(diametroEstaca)[2]
    rp = valores_rp(listaTipoSolo, listaNspt)
    alpha = searchCorrAlphaDc(listaTipoSolo[0], tipoEstaca)[0]

    listaValoresRp = []
    for i in range(len(listaTipoSolo)):
        listaValoresRp.append(alpha * rp[i] * areaEstaca)    

    return listaValoresRp


def calc_rl(nspt):

    #if nspt < 3:
        #nspt = 3

    #elif nspt > 15:
       # nspt = 15
    
    #else:
        #nspt = nspt

    rl = 10 * ((nspt / 3) + 1)

    return rl


def valores_rl(listaNspt):

    lista_val_rl = []

    for i in range(len(listaNspt)):
        lista_val_rl.append(calc_rl(listaNspt[i]))
    
    return lista_val_rl


def valoresRl(listaNspt, listaTipoSolo, tipoEstaca, diametroEstaca):

    perimEstaca = prop_geom_estacas(diametroEstaca)[1]
    rl = valores_rl(listaNspt)
    beta = searchCorrBetaDc(listaTipoSolo[0], tipoEstaca)[0]

    listaValoresRl = []
    for i in range(len(listaTipoSolo)):
        listaValoresRl.append(beta * rl[i] * perimEstaca)


    return listaValoresRl