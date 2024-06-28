from colorama import init, Fore, Back, Style
from PyTie import PyTie as pytie
import random as random
import locale as locale
from Ctrl import Ctrl
import math as math
import time as time
import sys as sys

class Mont:
    init(autoreset=True)

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    def routine0001():
        hc = 7
        return hc
    
    def routine0002():
        vf = 1   

        if(vf == 1):
            print(f"Velocidade 1: {Fore.GREEN}{vf}{Fore.RESET} m/s")
        elif(vf > 1 or vf < 1):
            print(f"Velocidade 1: {Fore.GREEN}{vf}{Fore.RESET} m/s")
        elif(vf >> 1):
            print(f"Velocidade 1: {Fore.GREEN}{vf}{Fore.RESET} m/s")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()
        return vf
    
    def routine0003(de, pi, Qf):
        v2 = pytie.equad11(de, pi, Qf)
        print(f"Velocidade 2: {Fore.GREEN}{round(v2, 2)}{Fore.RESET} m/s")
        return v2
    
    def routine0004(dt, pi, Qf):
        v3 = pytie.equad12(dt, pi, Qf)
        print(f"Velocidade 3: {Fore.GREEN}{round(v3, 2)}{Fore.RESET} m/s")
        return v3
    
    def routine0005(ds, pi, Qf):
        v4 = pytie.equad13(ds, pi, Qf)
        print(f"Velocidade 4: {Fore.GREEN}{round(v4, 2)}{Fore.RESET} m/s")
        return v4
    
    def routine0006(hc, vf, alpha, de, cl):
        da = pytie.equad08(alpha)
        Qf = pytie.equad10(da, de, hc, vf)
        if(Qf == 0):
            Qf = "Não há vazão volumétrica."
        elif(Qf < 200 or Qf > 300):
            Ctrl.routine0026(Qf, alpha) # Para ver Zona: Não Operação, altere para print().
        return Qf
    
    def routine0007(hc, de, hd):
        hq = pytie.equad09(hc, de, hd)
        print(f"Altura da queda d'água: {Fore.MAGENTA}{hq}{Fore.RESET} m")
        print()
        return hq
    
    def routine0008(z1, z2, vf, v2, g, y, P1, vm1_2, ks_2, ks_3, ks_5):
        H1 = pytie.equad04(z1, vf, g, y, P1)

        hs_1 = pytie.equad07(ks_2, vm1_2, g) / 100
        hs_2 = pytie.equad07(ks_3, vm1_2, g) / 100
        hs_3 = pytie.equad07(ks_5, vm1_2, g) / 100

        hs_t = hs_1 + hs_2 + hs_3 
        hs_t = round(hs_t)

        P2 = round((pytie.equad05(H1, z2, v2, g, y) - hs_t), 2)

        return P2

    def routine0009(z2, z3, v2, v3, g, y, P2, f, L, dt, vm2_3, ks_3): 
        H2 = pytie.equad04(z2, v2, g, y, P2)

        hf = round(pytie.equad06(f, L, dt, vm2_3, g)) / 100
        hs_1 = round(pytie.equad07(ks_3, vm2_3, g)) / 100

        h_t = hs_1 + hf
        
        P3 = round((pytie.equad05(H2, z3, v3, g, y) - h_t), 2) * (-1)

        return P3
    
    def routine0010(z3, z4, v3, v4, g, y, P3, ks_4, vm3_4, c_mano):
        H3 = pytie.equad04(z3, v3, g, y, P3)

        hs_1 = round(pytie.equad07(ks_4, vm3_4, g)) / 100

        P4 = round((pytie.equad05(H3, z4, v4, g, y) - hs_1 + c_mano), 2)

        return P4
    
    def routine0011(ds, hq, y):
        z5 = pytie.equad21(ds, hq)
        P5 = pytie.equad01(y, z5)
        return P5
    
    def routine0012(Q, nt, p, hq):
        Pw = pytie.equad02(Q, nt, p, hq) / 1000
        print(f"Produção energética: {Fore.YELLOW}{round(Pw, 2)}{Fore.RESET} megawatts (MW)")
        print()
        return Pw
    
    def routine0013(y, hs):
        for z in range(0, (hs + 5), 5):
            P = pytie.equad01(y, z)
            P_format = locale.format_string('%.2f', P, grouping=True)

            print(f"Pressão contra a estrutura a {z} m: {Fore.CYAN}{P_format}{Fore.RESET} Pa")
    
    def routine0014(alpha):
        estavel = random.randint(0, 10)
        if (estavel == 0):
            print(f"{Back.WHITE}{Fore.BLACK}Estabilidade estrutural da usina comprometida.{Fore.RESET}{Back.RESET}")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()
        else: 
            print(f"{Back.BLACK}{Fore.WHITE}Estabilidade estrutural da usina adequada.{Fore.RESET}{Back.RESET}")
        return estavel
        
    def routine0016(estavel, alpha):
        erosao = random.randint(0, 10)

        if(estavel == 0):
            print(f"{Back.WHITE}{Fore.BLACK}Estabilidade estrutural da usina comprometida (Revisto).{Fore.RESET}{Back.RESET}")
            print()

        else:
            print(f"{Back.BLACK}{Fore.WHITE}Estabilidade estrutural da usina adequada (Revisto).{Fore.RESET}{Back.RESET}")
            print()

        if(erosao == 0):
            print(f"{Back.WHITE}{Fore.BLACK}Integridade do leito comprometida.{Fore.RESET}{Back.RESET}")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()
        else:
            print(f"{Back.BLACK}{Fore.GREEN}Erosão do leito não apresenta risco.{Fore.RESET}{Back.RESET}")
            print()

            
    def routine0017():
        invasao = random.randint(0, 10)
        if(invasao == 0):
            print(f"{Back.BLACK}{Fore.RED}Presença não autorizada dentro da zona de segurança.{Fore.RESET}{Back.RESET}")
            print()

            
    def routine0018(alpha):
        vibracao = random.randint(0, 10)
        if (vibracao == 0):
            print()
            print(f"{Back.BLACK}{Fore.RED}Vibrações das turbinas acima do normal.{Fore.RESET}{Back.RESET}")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()

    def routine0020(P4, P5, Qf):

        zona_op = ""

        if(P4 > 900000 and P5 > 400000):
            zona_op = "Regular"
        elif(P4 > 900000 and 400000 > P5 > 380000):
            zona_op = "Moderada"
        elif(900000 > P4 > 800000 and 380000 > P5 > 370000):
            zona_op = "Intermediária"
        elif(P4 < P5 or Qf < 200):
            zona_op = "Não Operação"
        elif(P4 < 700000 and 360000 > P5 > 350000):
            zona_op = "Baixa"
        else:
            zona_op = "Não é possível determinar a zona de operação."
        return zona_op
    
    def routine0021():
        print(f"{Back.BLACK}{Fore.GREEN}Todos os processos foram concluídos.{Fore.RESET}{Back.RESET}")
        return True