from PyTie import PyTie as pytie
import random as random
import math as math
import time as time
from Mont import Mont
from Excp import Excp 
from Ctrl import Ctrl
import sys as sys
from datetime import datetime

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

    '''
    if(excp == 0):
        Excp.routine0033()
        Excp.routine0044()
        print("Danos: diversas tubulações foram rompidas, incluindo o conduto forçado.")
        print(f"Ações recomendadas: {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r4}.")
        sys.exit()

    elif(excp == 13):
        estado = Excp.routine0034
        if (estado == 0):
            Excp.routine0044()
            print("Transmissão de energia interrompida.")

        data_atual = datetime.now()

        print(f"A usina está desligada. No dia {data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}, ocorreu um blackout na instalação.")
        print("Não houve danos aparentes aos equipamentos da usina.")
        print(f"Ações recomendadas: {Excp.r5}, {Excp.r6}.")
        sys.exit()

    elif(excp == 26):
        Excp.routine0035()
        Excp.routine0044()
        print("Não ocorreram danos significativos à estrutura e equipamentos da usina.")
        print(f"Ações recomendadas: {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r7}")
        sys.exit()

    elif(excp == 39):
        Excp.routine0036()
        Excp.routine0044()
        print("Danos: rompimento na lateral do casco da usina.")
        print(f"Ações recomendadas: {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r4}.")
        sys.exit()

    elif(excp == 52):
        Excp.routine0037()
        Excp.routine0044()
        print("Sistema anti-incêndio acionado.")
        print("Danos: rompimento na lateral do casco da usina.")
        print(f"Ações recomendadas: {Excp.r7}, {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r9}, {Excp.r10}.")
        sys.exit()

    elif(excp == 65):
        Excp.routine0038()
        print(f"Ações recomendadas: {Excp.r1}, {Excp.r2}, {Excp.r3}.")
        sys.exit()

    elif(excp == 78):
        Excp.routine0039()
        sys.exit()

    elif(excp == 91):
        Excp.routine0040()
        print("Danos: o impacto não causou danos consideráveis.")
        print(f"Ações recomendadas: {Excp.r1}, {Excp.r2}, {Excp.r11}.")
        sys.exit()

    elif(excp == 104):
        Excp.routine0041()
        Excp.routine0044()
        print("A transmissão de energia foi interrompida.")
        print("Danos: além do cabo de transmissão de energia, outros equipamentos foram danificados.")
        print(f"Ações recomendadas: {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r14}, {Excp.r15}")

    elif(excp == 117):
        Excp.routine0042()
        Excp.routine0044()
        print("Danos: além dos danos causados à estrutura por causa do desmebramento, podem ter ocorrido danos ao ambiente próximo à usina.")
        print(f"Ações recomendadas: {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r16}")

    elif(excp == 117):
        Excp.routine0042()
        Excp.routine0044()

    elif(excp == 130):
        Excp.routine0043()
        Excp.routine0044()
        print("Danos: além da perda total do conjunto, outros equipamentos foram seriamente danificados.")
        print(f"Ações recomendadas: {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r17}.")

    elif(excp == 143):
        Excp.routine0045(alpha)
        print(f"Ações recomendadas: {Excp.r3}, {Excp.r1}.")
        
    '''
    
    hc = Mont.routine0001()
    
    if(hc <= 0):
        alpha = 30
    elif(hc == 1):
        alpha = 25
    elif(hc == 2):
        alpha = 21
    elif(hc == 3):
        alpha = 18
    elif(hc == 4):
        alpha = 15
    elif(hc == 5):
        alpha = 12
    elif(hc == 6):
        alpha = 10
    elif(hc == 7):
        alpha = 8
    elif(hc == 8):
        alpha = 5
    elif(hc == 9):
        alpha = 0
    
    print(f"Alfa: {alpha}")
    
    if(hc >= -6 and hc <= 7):
        print(f"Nível da água: {hc} m.")
    else:
        print(f"Nível da água: {hc} m.")
        Ctrl.routine0032(alpha)
        Mont.routine0021()
        sys.exit()

    vf = Mont.routine0002()

    Qf = Mont.routine0006(hc, vf, alpha, de, cl)

    v2 = Mont.routine0003(de, pi, Qf)
    
    v3 = Mont.routine0004(dt, pi, Qf)
    
    v4 = Mont.routine0005(ds, pi, Qf)
    
    hq = Mont.routine0007(hc, de, hd)
    
    Mont.routine0008()
    
    Mont.routine0009()
    
    Mont.routine0010()
    
    P5 = Mont.routine0011(ds, hq, y)
    
    Pw = Mont.routine0012(Qf, nt, p, hq)
        
    Mont.routine0013(y, hs)
    
    estavel = Mont.routine0014(alpha)
        
    Mont.routine0016(estavel, alpha)
    
    Mont.routine0017()
    
    Mont.routine0018(alpha)
        
    Mont.routine0020()        
    
if __name__ == "__main__":
    main()
