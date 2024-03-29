import pandas as pd
from sympy import cot
import math


class DimCisalhamento_mod2:

    listaVigas = []

    def __init__(self, nome, alfa, teta, vd, h, d, b, fck, fywk):
        self.nome = nome
        self.vd = vd
        self.h = h
        self.d = d
        self.b = b

        self.fck = fck
        self.fcd = fck / 14
        self.fctd = (0.21 * (fck ** (2 / 3)) / 14)
        self.fctm = ((0.3 * pow(fck, (2 / 3))) / 10)

        self.fywk = fywk
        self.fywd = fywk / 11.5

        self.alfa = math.radians(alfa)
        self.teta = math.radians(teta)

        DimCisalhamento_mod2.listaVigas.append(self)
        
    def calcVrd2(self):

        vRd2 = 0.54 * ( 1 - (self.fck / 250)) * self.fcd * self.b * self.d * pow(math.sin(self.teta), 2) * (cot(self.alfa) + cot(self.teta))

        if vRd2 < self.vd:
            print (f'Biela comprimida esmagada. Aumentar dimensões da viga. Vrd2: {vRd2} kN < Vsd: {self.vd} kN')
            exit()

        return round(vRd2, 2)
    

    def calcAsw_min(self):

        asw_min = (20 * self.fctm * self.b) / (self.fywk / 10)

        return round(asw_min, 2)
    

    def calc_vc(self):

        vc0 = 0.6 * self.fctd * self.b * self.d
        vc1 = vc0 * ((self.calcVrd2() - self.vd) / (self.calcVrd2() - vc0))
        
        if self.vd > vc0:
            vc = vc1
        
        else:
            vc = vc0

        return round(vc, 2)


    def calc_vsw(self):

        vsw = self.vd - self.calc_vc()

        if vsw <= 0:
            print ('Vc' f'{self.calc_vc()}' 'kN >= Vsd' f'{self.vd}' 'kN. Utilizar armadura mínima: ' f'{self.calcAsw_min()}' 'cm²/cm')
            exit()
        
        return round(vsw, 2)
    

    def calcAsw_s(self):

        asw_s = (self.calc_vsw() / (0.9 * self.d * self.fywd * (cot(self.alfa) + cot(self.teta)) * math.sin(self.alfa))) * 100
      
        return round(asw_s, 2)


    def calcEfetivo(self):
          
        if self.calcAsw_s() < self.calcAsw_min():
            asw_efe = self.calcAsw_min()
        
        else:
            asw_efe = self.calcAsw_s()

        return round(asw_efe, 2)


    def resultados(self):

        resultados = {
            'Nome': [self.nome],
            'Vsd (kN)': [self.vd],
            'Vrd2 (kN)': [self.calcVrd2()],
            'Vc (kN)': [self.calc_vc()],
            'Vsw (kN)': [self.calc_vsw()],
            'Asw,mín (cm²/m)': [self.calcAsw_min()],
            'Asw,calc (cm²/m)': [self.calcAsw_s()],
            'Asw,efetivo (cm²/m)': [self.calcEfetivo()]

        }

        df_results = pd.DataFrame(resultados)

        return df_results