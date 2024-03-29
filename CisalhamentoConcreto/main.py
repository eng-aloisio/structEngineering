from modelo1 import DimCisalhamento_mod1
from modelo2 import DimCisalhamento_mod2

#ENTRADA DE DADOS

#GEOMETRIA
h = 40 #cm
d = 36 #cm
b = 12 #cm

#MATERIAIS
fck = 20 #Mpa
fywk = 500 #MPa

#ESFORÇO DE CÁLCULO 
vd = 30 * 1.4 #kN

#ALFA E TETA (MODELO II)
alfa = 90 #Graus
teta = 30 #Graus

#SAÍDA DE DADOS

#V1
viga_01_mod1 = DimCisalhamento_mod1('V1', vd, h, d, b, fck, fywk)
viga_01_mod2 = DimCisalhamento_mod2('V1', alfa, teta, vd, h, d, b, fck, fywk)

print(viga_01_mod1.resultados())
print(viga_01_mod2.resultados())





