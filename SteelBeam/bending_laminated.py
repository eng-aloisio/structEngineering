from auxiliar import profile_data, profile_list
import math
import pandas as pd



# FLT necessita de verificação manual para confirmar resultados
def flt(product, profile, fy, lb, cb):
    # fy = kN/cm²
    # E = kN/cm²

    modE = 20000 # Verificar necessidade de modificação antes de utilizar
    ya1 = 1.1
    lp = profile_data(product, profile)

    mp = lp[12] * fy
    lamb = lb / lp[15]
    lamb_p = 1.76 * pow((modE / fy), 0.5) 

    if lamb <= lamb_p:
        mRdx_flt = mp / ya1
    
    else:
        sigma_r = 0.3 * fy
        beta1 = ((fy - sigma_r) / (modE * lp[18])) * lp[10]
        lamb_r = (1.38 * pow(lp[13] * lp[18], 0.5) / (lp[15] * lp[18] * beta1)) * pow(1 + pow(1 + (27 * lp[19] * pow(beta1, 2) / lp[13]), 0.5), 0.5)

        if lamb <= lamb_r:
            mR = (fy - sigma_r) * lp[10]
            mRdx_flt = (cb / ya1) * (mp - ((mp - mR) / (lamb_r - lamb_p) * (lamb - lamb_p)))
        
        else:
            mCr = ((cb * pow(math.pi, 2) * modE * lp[13]) / pow(lb, 2)) * pow((lp[19] / lp[13]) * (1 + 0.039 * lp[18] * pow(lb, 2) / lp[19]), 0.5)
            mRdx_flt = mCr / ya1

    return mRdx_flt


# FLM necessita de verificação manual para confirmar resultados
def flm(product, profile, fy):
  
    modE = 20000 # Verificar necessidade de modificação antes de utilizar
    ya1 = 1.1

    lp = profile_data(product, profile)
    mp = lp[12] * fy

    lamb = (lp[3] / 2) / lp[5]
    lamb_p = 0.38 * pow(modE / fy, 0.5)

    if lamb <= lamb_p:
        mRdx_flm = mp / ya1
    
    else:
        sigma_r = 0.3 * fy
        lamb_r = 0.83 * pow(modE / (fy - sigma_r), 0.5)

        if lamb <= lamb_r:
            mR = (fy - sigma_r) * lp[10]
            mRdx_flm = (1 / ya1) * (mp - ((mp - mR) / (lamb_r - lamb_p) * (lamb - lamb_p)))

        else:
            mCr = 0.69 * lp[10] * modE / pow(lamb, 2)
            mRdx_flm = mCr / ya1
    
    return mRdx_flm


# FLM necessita de verificação manual para confirmar resultados
def fla(product, profile, fy):
   
    modE = 20000 # Verificar necessidade de modificação antes de utilizar
    ya1 = 1.1

    lp = profile_data(product, profile)
    mp = lp[12] * fy

    lamb = (lp[6] / 2) / lp[4]
    lamb_p = 3.76 * pow(modE / fy, 0.5)

    if lamb <= lamb_p:
        mRdx_fla = mp / ya1
    
    else:
        lamb_r = 5.70 * pow(modE / fy, 0.5)

        if lamb <= lamb_r:
            mr = fy * lp[10]
            mRdx_fla = (1 / ya1) * (mp - ((mp - mr) / (lamb_r - lamb_p) * (lamb - lamb_p)))

        else:
            print('Viga de alma esbelta, escolha um perfil com tw maior') # Implementar o anexo H posteriormente

    return mRdx_fla


def bending_verif(product, profile, fy, lb, cb, mD):

    mRdx_flt = flt(product, profile, fy, lb, cb)
    mRdx_flm = flm(product, profile, fy)
    mRdx_fla = fla(product, profile, fy)

    mRdx_list = [mRdx_flt, mRdx_flm, mRdx_fla]
    mRdx_min = min(mRdx_list)

    efic = (mD / mRdx_min) * 100
    efic_flt = (mD / mRdx_flt) * 100
    efic_flm = (mD / mRdx_flm) * 100
    efic_fla = (mD / mRdx_fla) * 100

    if efic <= 100:
        msg = 'Perfil aprovado'
    
    else:
        msg = 'Perfil reprovado'

    export_results = [efic, efic_flt, efic_flm, efic_fla, msg]

    return export_results


def process_dataset(product, fy, lb, cb, mD):
    
    profileList = profile_list(product)

    results = []

    for i in range(len(profileList)):
        print(f'{round((i / len(profileList)) * 100, 0)}%')
        results.append(bending_verif(product, profileList[i], fy, lb, cb, mD))

    final_results = {
        'Bitola': profileList,
        'Resultados': results
    }

    df = pd.DataFrame(final_results)

    return df







#TESTES

print(process_dataset('Laminados', 25, 300, 1, 7000))

