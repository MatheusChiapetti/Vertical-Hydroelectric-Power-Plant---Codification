from PyTie import PyTie as pytie
import random as random
from Ctrl import Ctrl
import math as math
import time as time
import sys as sys

class Mont:
    
    def routine0001():
        hc = 7
        return hc
    
    def routine0002():
        vf = 1   

        if(vf == 1):
            print(f"Velocidade da água: {vf} m/s")
        elif(vf > 1 or vf < 1):
            print(f"Velocidade da água: {vf} m/s")
        elif(vf >> 1):
            print(f"Velocidade da água: {vf} m/s")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()
        return vf
    
    def routine0003(de, pi, Qf):
        v2 = pytie.equad11(de, pi, Qf)
        print(f"Velocidade 2: {round(v2, 2)} m/s")
        return v2
    
    def routine0004(dt, pi, Qf):
        v3 = pytie.equad12(dt, pi, Qf)
        print(f"Velocidade 3: {round(v3, 2)} m/s")
        return v3
    
    def routine0005(ds, pi, Qf):
        v4 = pytie.equad13(ds, pi, Qf)
        print(f"Velocidade 4: {round(v4, 2)} m/s")
        return v4
    
    def routine0006(hc, vf, alpha, de, cl):
        da = pytie.equad08(alpha)
        Qf = pytie.equad10(da, de, hc, vf)
        if(Qf == 0):
            print("Não há vazão volumétrica.")
        elif(Qf < 200 or Qf > 300):
            Ctrl.routine0026(Qf, alpha)
        print(f"Vazão volumétrica: {round(Qf, 2)} m³/s")
        return Qf
    
    def routine0007(hc, de, hd):
        hq = pytie.equad09(hc, de, hd)
        print(f"Altura da queda d'água: {hq} m")
        return hq
    
    def routine0008(): # TERMINAR!
        return
    
    def routine0009(): # TERMINAR!
        return
    
    def routine0010(): # TERMINAR!
        return
    
    def routine0011(ds, hq, y):
        z5 = pytie.equad21(ds, hq)
        P = pytie.equad01(y, z5)
        print(f"Pressão no leito (P5): {P} Pa")
        return P
    
    def routine0012(Q, nt, p, hq):
        Pw = pytie.equad02(Q, nt, p, hq) / 1000
        print(f"Produção energética: {round(Pw, 2)} megawatts (MW)")
        return Pw
    
    def routine0013(y, hs):
        for z in range(0, (hs + 5), 5):
            P = pytie.equad01(y, z)
            print(f"Pressão contra a estrutura a {z} m: {P} Pa")
    
    def routine0014(alpha):
        estavel = random.randint(0, 10)
        if (estavel == 0):
            print("Estabilidade estrutural da usina comprometida.")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()
        else: 
            print("Estabilidade estrutural da usina adequada.")
        return estavel
        
    def routine0016(estavel, alpha):
        erosao = random.randint(0, 10)

        if(estavel == 0):
            print(f"Estabilidade estrutural da usina comprometida.")
        else:
            print(f"Estabilidade estrutural da usina adequada.")

        if(erosao == 0):
            print("Integridade do leito comprometida.")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()
        else:
            return print("Erosão do leito não apresenta risco.")
            
    def routine0017():
        invasao = random.randint(0, 10)
        if(invasao == 0):
            return print(f"Presença não autorizada dentro da zona de segurança.")
            
    def routine0018(alpha):
        vibracao = random.randint(0, 10)
        if (vibracao == 0):
            print("Vibrações das turbinas acima do anormal.")
            Ctrl.routine0032(alpha)
            Mont.routine0021()
            sys.exit()

    def routine0020():
        return
    
    def routine0021():
        print("Todos os processos foram concluídos")
        return True