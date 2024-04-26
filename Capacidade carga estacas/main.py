from funcCapCargDC import valores_rp, valoresRp, valores_rl, valoresRl, calc_rl
from funcCapCargAoki import resultAoki

tipo = 'HCM'    #HCM, Escavada, Escavada (b) (Decourt-Quaresma), Raiz
diametro = 0.30      #m
carga_adm_esperada = 170    #kN


nspt =   [0,  1,  1,  3,  6,  10, 11, 16, 30, 50, 50, 50, 50, 50, 50]
solo = [23, 23, 23, 23, 32, 32, 32, 32, 32, 12, 12, 12, 12, 12, 12]      #Usuário pode verificar os códigos no arquivo "convencoes.txt"


#EXECUÇÕES

print(valoresRl(nspt, solo, tipo, diametro))
print(valoresRp(solo,nspt, tipo, diametro))
