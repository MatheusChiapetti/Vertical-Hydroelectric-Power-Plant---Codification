from colorama import init, Fore, Back, Style
from PyTie import PyTie as pytie
from datetime import datetime
import random as random
import locale as locale
from Mont import Mont
from Excp import Excp 
from Ctrl import Ctrl
import math as math
import time as time
import sys as sys

def main():

    init(autoreset=True)

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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

    '''
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
 

    P1 = 0
    
    excp = random.randint(0, 143)

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

    print()

    if(excp == 0):
        Excp.routine0033()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} diversas tubulações foram rompidas, incluindo o conduto forçado.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r4}.")
        print()
        sys.exit()

    elif(excp == 13):
        estado = Excp.routine0034()    
        print(f"{Back.BLACK}{Fore.RED}Sistemas Offline.{Fore.RESET}{Back.RESET}")
        print()
        if (estado == 0):
            Excp.routine0044()
            print()
        data_atual = datetime.now()

        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu um blackout na instalação.")
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} Não houve danos aparentes aos equipamentos da usina.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r5}, {Excp.r6}.")
        print()
        sys.exit()

    elif(excp == 26):
        Excp.routine0035()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} Não ocorreram danos significativos à estrutura e equipamentos da usina.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r7}")
        print()
        sys.exit()

    elif(excp == 39):
        Excp.routine0036()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} rompimento na lateral do casco da usina.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r4}.")
        print()
        sys.exit()

    elif(excp == 52):
        Excp.routine0037()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}{Fore.YELLOW}Sistema anti-incêndio acionado.{Fore.RESET}{Back.RESET}")
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} rompimento na lateral do casco da usina.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r7}, {Excp.r1}, {Excp.r2}, {Excp.r3}, {Excp.r9}, {Excp.r10}.")
        print()
        sys.exit()

    elif(excp == 65):
        Excp.routine0038()
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r1}, {Excp.r2}, {Excp.r3}.")
        print()
        sys.exit()

    elif(excp == 78):
        Excp.routine0039(alpha)
        sys.exit()

    elif(excp == 91):
        Excp.routine0040()
        print(f"{Back.BLACK}Danos:{Back.RESET} o impacto não causou danos consideráveis.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r1}, {Excp.r2}, {Excp.r11}.")
        print()
        sys.exit()

    elif(excp == 104):
        Excp.routine0041()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} além do cabo de transmissão de energia, outros equipamentos foram danificados.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r14}, {Excp.r15}")
        print()
        sys.exit()

    elif(excp == 117):
        Excp.routine0042()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} além dos danos causados à estrutura por causa do desmebramento, podem ter ocorrido danos ao ambiente próximo à usina.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r16}")
        print()
        sys.exit()

    elif(excp == 130):
        Excp.routine0043()
        Excp.routine0044()
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} além da perda total do conjunto, outros equipamentos foram seriamente danificados.")
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r3}, {Excp.r1}, {Excp.r12}, {Excp.r13}, {Excp.r17}.")
        print()
        sys.exit()

    elif(excp == 143):
        Excp.routine0045(alpha)
        print(f"{Back.BLACK}Ações recomendadas:{Back.RESET} {Excp.r3}, {Excp.r1}.")
        print()
        sys.exit()
    
    if(hc >= -6 and hc <= 7):
        print(f"Nível da água: {Fore.BLUE}{hc}{Fore.RESET} m.")
    else:
        print(f"Nível da água: {Fore.BLUE}{hc}{Fore.RESET} m.")
        Ctrl.routine0032(alpha)
        Mont.routine0021()
        sys.exit()
        
    print()

    vf = Mont.routine0002()

    Qf = Mont.routine0006(hc, vf, alpha, de, cl)

    v2 = Mont.routine0003(de, pi, Qf)
    
    v3 = Mont.routine0004(dt, pi, Qf)
    
    v4 = Mont.routine0005(ds, pi, Qf)
    print()

    print(f"Vazão volumétrica: {Fore.YELLOW}{round(Qf, 2)}{Fore.RESET} m³/s")
    print()

    hq = Mont.routine0007(hc, de, hd)

    L = pytie.equad22(hd, de, sec)

    z1 = pytie.equad17(de, hc, hd, hr)

    z2 = pytie.equad18(de, hd, hr)

    z3 = pytie.equad19(dt, hr)

    z4 = pytie.equad20(hr, dt)

    z5 = pytie.equad21(ds, hq)
        
    Pw = Mont.routine0012(Qf, nt, p, hq)

    c_mano = pytie.equad03(Pw, y, Qf, nt)  

    vm1_2 = pytie.equad14(vf, v2)

    vm2_3 = pytie.equad15(v2, v3)

    vm3_4 = pytie.equad16(v3, v4)
    
    P2 = Mont.routine0008(z1, z2, vf, v2, g, y, P1, vm1_2, ks_2, ks_3, ks_5)
    
    P3 = Mont.routine0009(z2, z3, v2, v3, g, y, P2, f, L, dt, vm2_3, ks_3)

    P4 = Mont.routine0010(z3, z4, v3, v4, g, y, P3, ks_4, vm3_4, c_mano)

    P5 = Mont.routine0011(ds, hq, y)

    P2_format = locale.format_string('%.2f', P2, grouping=True)
    P3_format = locale.format_string('%.2f', P3, grouping=True)
    P4_format = locale.format_string('%.2f', P4, grouping=True)
    P5_format = locale.format_string('%.2f', P5, grouping=True)

    print(f"Pressão 2: {Fore.BLUE}{P2_format}{Fore.RESET} Pa")
    print(f"Pressão 3: {Fore.BLUE}{P3_format}{Fore.RESET} Pa")
    print(f"Pressão 4: {Fore.BLUE}{P4_format}{Fore.RESET} Pa")
    print(f"Pressão 5: {Fore.BLUE}{P5_format}{Fore.RESET} Pa")
    print()

    Mont.routine0013(y, hs)
    print()

    estavel = Mont.routine0014(alpha)
        
    Mont.routine0016(estavel, alpha)

    Mont.routine0017()

    Mont.routine0018(alpha)

    zona_op = Mont.routine0020(P4, P5, Qf) 

    if(zona_op == "Regular"):
        print(f"Zona de operação: {Fore.GREEN}{zona_op}")    
    elif(zona_op == "Moderada"):
        print(f"Zona de operação: {Fore.CYAN}{zona_op}")  
    elif(zona_op == "Intermediária"):
        print(f"Zona de operação: {Fore.YELLOW}{zona_op}")  
    elif(zona_op == "Baixa"):
        print(f"Zona de operação: {Fore.MAGENTA}{zona_op}")  
    elif(zona_op == "Não Operação"):
        print(f"Zona de operação: {Fore.RED}{zona_op}")  
    else:
        print(f"Zona de operação: {Back.WHITE}{Fore.BLACK}{zona_op}")  

    print()

if __name__ == "__main__":
    main()
