from tabelasParametros import parametro_aoki_tabela, fator_correcao_aoki
import math
import pandas as pd

 
def searchParamAoki(tipoSolo):      #Função que procura no dataFrame os parametros K e Alpha para o tipo de solo escolhido
                                    
    df = parametro_aoki_tabela()
    df2 = df.loc[df['Solo'] == tipoSolo]
    lista_K = df2['K (kPa)'].tolist()
    lista_alpha = df2['Alpha'].tolist()

    lista_parametros_aoki = [lista_K[0], lista_alpha[0]]

    return lista_parametros_aoki


def searchCorrAoki(tipoEstaca):     #Função que procura no dataFrame os parametros F1 e F2 para o tipo de estaca escolhida

    df = fator_correcao_aoki()
    df2 = df.loc[df['Tipo de estaca'] == tipoEstaca]
    lista_F1 = df2['F1'].tolist()
    lista_F2 = df2['F2'].tolist()

    lista_correcao_aoki = [lista_F1[0], lista_F2[0]]

    return lista_correcao_aoki                      


def calc_rp_aoki(tipoSolo, tipoEstaca, nspt):       #Função que calcula o valor de rp para um determinado Nspt

    valor_K = searchParamAoki(tipoSolo)[0]
    valor_F1 = searchCorrAoki(tipoEstaca)[0]

    rp = valor_K * nspt / valor_F1      #rp em kPa

    return rp


def calc_rl_aoki(tipoSolo, tipoEstaca, nspt):       #Função que calcula o valor de rl para um determinado Nspt

    valor_K = searchParamAoki(tipoSolo)[0]
    valor_F2 = searchCorrAoki(tipoEstaca)[1]
    valor_alpha = searchParamAoki(tipoSolo)[1]


    rl = valor_alpha * valor_K * nspt / valor_F2

    return rl


def prop_geom_estacas(diametro):        #Função que devolve o diâmetro, perímetro e área da estaca

    perimetro_estaca = diametro * math.pi
    area_estaca = pow(diametro, 2) * math.pi / 4

    resultados_prop_geom = [diametro, perimetro_estaca, area_estaca]

    return resultados_prop_geom


def valores_K(listaTipoSolos):     #Função que devolve os valores de K para cada tipo de solo escolhido pelo usuário           
   
    lista_valores_K = []
    for tipo_solo in listaTipoSolos:
        lista_valores_K.append(searchParamAoki(tipo_solo)[0])

    return lista_valores_K


def valores_rp(listaTipoSolos, tipoEstaca, listaNspt):      #Função que calcula os valores de rp para cada tipo de solo escolhido pelo usuário e para cada Nspt

    listaNspt.append(listaNspt[-1])
    lista_valores_rp = []
    
    for i in range(len(listaTipoSolos)):
        lista_valores_rp.append(calc_rp_aoki(listaTipoSolos[i], tipoEstaca, listaNspt[i + 1]))

    listaNspt.pop()

    return lista_valores_rp


def valoresRp(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca):        #Função que calcula os valores de Rp para cada valor de rp na lista

    areaEstaca = prop_geom_estacas(diametroEstaca)[2]
    rp = valores_rp(ListaTipoSolo, tipoEstaca, listaNspt)

    listaValoresRp = []
    for i in range(len(ListaTipoSolo)):
        listaValoresRp.append(rp[i] * areaEstaca)

    return listaValoresRp


def valores_rl(listaTipoSolos, tipoEstaca, listaNspt):

    lista_valores_rl = []

    for i in range(len(listaTipoSolos)):
        lista_valores_rl.append(calc_rl_aoki(listaTipoSolos[i], tipoEstaca, listaNspt[i]))
   
    return lista_valores_rl


def valoresRl(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca):

    perimEstaca = prop_geom_estacas(diametroEstaca)[1]
    rl = valores_rl(ListaTipoSolo, tipoEstaca, listaNspt)

    listaValoresRl = []
    for i in range(len(ListaTipoSolo)):
        listaValoresRl.append(rl[i] * perimEstaca)
    
    return listaValoresRl


def acumRl(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca):

    listaValoresRl = valoresRl(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca)

    series = pd.Series(listaValoresRl)
    lista_acumulada_Rl = series.cumsum()
    

    return lista_acumulada_Rl


def resistenciaTotal(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca):

    lateralAcumulado =  acumRl(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca)
    resistenciaPonta =  valoresRp(ListaTipoSolo, tipoEstaca, listaNspt, diametroEstaca)
    
    resistTotal = []

    for i in range(len(ListaTipoSolo)):
        resistTotal.append(lateralAcumulado[i] + resistenciaPonta[i])

    return resistTotal


def paNbr6122(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca):

    resistTotal = resistenciaTotal(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca)
    
    pa6122 = []

    for i in range(len(resistTotal)):
        pa6122.append(resistTotal[i] / 2)

    return pa6122


def paEscavadas(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca):

    valoresRlacum = acumRl(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca)
    
    paEscav = []

    for i in range(len(valoresRlacum)):
        paEscav.append(valoresRlacum[i] * 1.25)

    return paEscav


def paFinalAoki(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca):

    pa6122 = paNbr6122(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca)
    paEsc = paEscavadas(listaTipoSolo, tipoEstaca, lista_Nspt, diametroEstaca)
    paFinal = []

    for i in range(len(pa6122)):
        paFinal.append(min([pa6122[i], paEsc[i]]))

    return paFinal


def cotasPonta(ListaTipoSolo):

    cotasProf = []

    for i in range(len(ListaTipoSolo)):
        cotasProf.append((i + 1) * - 1)

    return cotasProf



#RESULTADOS


def resultAoki (ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca):

    resultCompletAoki = {
        'Cotas (m)': cotasPonta(ListaTipoSolo),
        'K (Kpa)': valores_K(ListaTipoSolo),
        'rp (kPa)': valores_rp(ListaTipoSolo, tipoEstaca, ListaNspt),
        'Rp (kN)': valoresRp(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'rl (kPa)': valores_rl(ListaTipoSolo, tipoEstaca, ListaNspt),
        'Rl (kN)': valoresRl(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'Rl acum. (kN)': acumRl(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'Rt (kN)': resistenciaTotal(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'Pa Nbr 6122 (kN)': paNbr6122(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'Pa Esc. (kN)': paEscavadas(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca),
        'Pa Final (kN)': paFinalAoki(ListaTipoSolo, tipoEstaca, ListaNspt, diametroEstaca)
    }

    dfResult = pd.DataFrame(resultCompletAoki)

    return dfResult




    

   