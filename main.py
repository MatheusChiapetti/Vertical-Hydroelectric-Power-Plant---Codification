from PyTie import PyTie as pytie
import random as random
import math as math
import time as time
from Mont import Mont
from Excp import Excp 
from Ctrl import Ctrl

'''
OBS IMPORTANTES (APAGAR QUANDO FINALIZAR):
1 - Usar "random.randint(0, 1)" para tomar as decisões binárias não quantitativas.
2 - As rotinas de emergência devem ser válidas/executadas antes das rotinas de monitoramento. 
3 - As rotinas de controle são chamadas dentro das rotinas de monitoramento.
'''

def main():

    y = 9800    # Peso específico do fluido.
    p = 1000    # Densidade do fluído.
    g = 9.8     # Aceleração da gravidade.
    f = 0.008   # Coeficiente de perda de carga distribuída.
    ks_1 = 0.3  # Ampliação gradual.
    ks_2 = 1    # Comporta aberta.
    ks_3 = 0.2  # Curva de 45°.
    ks_4 = 0.4  # Curva de 90°.
    ks_5 = 0.15 # Redução gradual.
    sec = 1.41  # Secante do ângulo θ (45°).
    nt = 0.9    # Rendimento da turbina.
    pi  = 3.14  # Pi.

    # Para hs = 50m, usar:
    de = 12 # Diâmetro da entrada do conduto.
    dt = 3  # Diâmetro do conduto na entrada da turbina.
    ds = 4  # Diâmetro do conduto na saída.
    cl = 12 # Comprimento da pá de captação.
    hl = 20 # Altura da pá de captação. 
    he = 20 # Altura emersa. 
    hs = 50 # Altura submersa.
    hd = 25 # Altura entre a base da entrada e a turbina.
    hr = 6  # Altura entre a turbina e o leito.

    alfa = 0

    Q = 285

    '''
    # Para hs = 40m, usar:
    de = 12 # Diâmetro da entrada do conduto.
    dt = 3  # Diâmetro do conduto na entrada da turbina.
    ds = 4  # Diâmetro do conduto na saída.
    cl = 12 # Comprimento da pá de captação.
    hl = 20 # Altura da pá de captação. 
    he = 20 # Altura emersa. 
    hs = 40 # Altura submersa.
    hd = 25 # Altura entre a base da entrada e a turbina.
    hr = 6  # Altura entre a turbina e o leito.
    ''' 
    
    # Rotinas de Emergência:

    # Condição para executar as emergências. Há a probabilidade de 8,28% de ocorrer uma emergência (13/157).
    excp = random.randint(0, 156)

    if(excp == 0):
        Excp.routine0033
    elif(excp == 13):
        Excp.routine0034
    elif(excp == 26):
        Excp.routine0035      
    elif(excp == 39):
        Excp.routine0036
    elif(excp == 52):
        Excp.routine0037
    elif(excp == 65):
        Excp.routine0038
    elif(excp == 78):
        Excp.routine0039
    elif(excp == 91):
        Excp.routine0040
    elif(excp == 104):
        Excp.routine0041
    elif(excp == 117):
        Excp.routine0042
    elif(excp == 130):
        Excp.routine0043
    elif(excp == 143):
        Excp.routine0044
    elif(excp == 156):
        Excp.routine0045  

    # Rotinas de Monitoramento:    
    
    hc = Mont.routine0001()
    
    vf = Mont.routine0002()

    Qf = Mont.routine0006()

    v2 = Mont.routine0003()
    
    v3 = Mont.routine0004()
    
    v4 = Mont.routine0005()
    
    hq = Mont.routine0007(hc, de, hd)
    
    Mont.routine0008()
    
    Mont.routine0009()
    
    Mont.routine0010()
    
    P5 = Mont.routine0011(ds, hq, y)
    
    Pw = Mont.routine0012(Q, nt, p, hq)
        
    Mont.routine0013(y, hs)
    
    estavel = Mont.routine0014()
        
    Mont.routine0016(estavel)
    
    Mont.routine0017()
    
    Mont.routine0018()
        
    Mont.routine0020()        
    
if __name__ == "__main__":
    main()
