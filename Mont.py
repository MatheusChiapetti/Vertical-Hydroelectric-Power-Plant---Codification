from PyTie import PyTie as pytie
import random as random
from Ctrl import Ctrl
import math as math
import time as time
import sys as sys

class Mont:
    
    def routine0001():
        hc = random.randint(-8, 9) # Altura entre a linha d'água e o topo da entrada.

        if(hc >= -6 and hc <= 7):
            print(f"Nível da água: {hc} m.")
        else:
            print(f"Nível da água: {hc} m.")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()

        return hc
    
    def routine0002():
        vf = random.randint(0, 5) # Velocidade do fluido fora da usina.    

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
    
    def routine0003():
        return
    
    def routine0004():
        return
    
    def routine0005():
        return
    
    def routine0006():
        return
    
    def routine0007(hc, de, hd):
        hq = pytie.equad09(hc, de, hd)
        print(f"Altura da queda d'água: {hq} m")
        return hq
    
    def routine0008():
        return
    
    def routine0009():
        return
    
    def routine0010():
        return
    
    def routine0011(ds, hq, y):
        z5 = pytie.equad21(ds, hq)
        P = pytie.equad01(y, z5)
        print(f"Pressão no leito: {P} Pa")
        return P
    
    def routine0012(Q, nt, p, hq):
        Pw = pytie.equad02(Q, nt, p, hq) / 1000
        print(f"Produção energética: {Pw} megawatts (MW)")
        return Pw
    
    def routine0013(y, hs):
        for z in range(0, hs, 5):
            P = pytie.equad01(y, z)
            print(f"Pressão: {P} Pa")
    
    def routine0014():
        estavel = random.randint(0, 10)
        if (estavel == 0):
            print("Estabilidade estrutural da usina comprometida.")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()
        else: 
            print("Estabilidade estrutural da usina adequada.")
        return estavel
        
    def routine0016(estavel):
        erosao = random.randint(0, 10)

        if(estavel == 0):
            print(f"Estabilidade estrutural da usina comprometida.")
        else:
            print(f"Estabilidade estrutural da usina adequada.")

        if(erosao == 0):
            print("Integridade do leito comprometida.")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()
        else:
            return print("Erosão do leito não apresenta risco.")
            
    def routine0017():
        invasao = random.randint(0, 10)
        if(invasao == 0):
            return print(f"Presença não autorizada dentro da zona de segurança.")
            
    def routine0018():
        vibracao = random.randint(0, 10)
        if (vibracao == 0):
            print("Vibrações das turbinas acima do anormal.")
            Ctrl.routine0032()
            Mont.routine0021()
            sys.exit()

    def routine0020():
        return
    
    def routine0021():
        print("Todos os processos foram concluídos")
        return True