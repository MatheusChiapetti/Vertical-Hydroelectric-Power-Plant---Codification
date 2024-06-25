from datetime import datetime
import random as random
import math as math
import time as time
import sys as sys

class Ctrl:
    
    def routine0022():
        print("As comportas estão sendo abertas.")
        time.sleep(2)
        print("As comportas foram totalmente abertas.")
    
    def routine0023():
        print("As comportas estão sendo fechadas.")
        time.sleep(2)
        print("As comportas foram totalmente fechadas.")
    
    def routine0024(alpha):
        if(alpha == 30):
            print("O ângulo a é máximo e o ajuste não pode ser feito.")
        print("As pás de captação estão sendo abertas.")
        time.sleep(2)
        print("As pás de captação foram ajustadas.")
        alpha = alpha + 1
        return alpha
    
    def routine0025(alpha):
        if(alpha == 0):
            print("O ângulo a é mínimo e o ajuste não pode ser feito.")
        elif(0 < alpha <= 30):
            print("As pás de captação estão sendo fechadas.")
            time.sleep(2)
            print("As pás de captação foram ajustadas.")
            alpha = alpha - 1
        return alpha
    
    def routine0026(Qf, alpha):
        if(alpha == 30 and Qf < 200):
            Ctrl.routine0032(alpha)
        elif(alpha != 30 and Qf < 200):
            Ctrl.routine0024(alpha)
            Qf = 285
        elif(alpha == 0 and Qf > 300):
            Ctrl.routine0032(alpha)
        elif(alpha != 0 and Qf > 300):
            Ctrl.routine0025(alpha)
            Qf = 285
        return Qf
    
    def routine0027():
        print("As pás de distribuição das turbinas estão sendo abertas.")
        time.sleep(2)
        print("As pás de distribuição das turbinas foram abertas.")
    
    def routine0028():
        print("As pás de distribuição das turbinas estão sendo fechadas.")
        time.sleep(2)
        print("As pás de distribuição das turbinas foram fechadas.")
    
    def routine0029():
        print("Aciondando sistemas de drenagem.")
        time.sleep(2)
        print("A água foi drenada dos condutos")
    
    def routine0030():
        data_atual = datetime.now()
        print(f"Não há nenhuma manutenção agendada para {data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}.")
    
    def routine0031(alpha):
        print("A usina será inicializada.")
        Ctrl.routine0022()
        Ctrl.routine0025(alpha)
        time.sleep(2)
        Ctrl.routine0027()
        time.sleep(2)
        print("A usina foi inicializada.")
    
    def routine0032(alpha):
        print("A usina será desligada.")
        print("Executando rotina 0025.")
        Ctrl.routine0025(alpha)
        time.sleep(2)
        print("Executando rotina 0028.")
        Ctrl.routine0028
        time.sleep(2)
        print("Executando rotina 0023.")
        Ctrl.routine0023
        time.sleep(2)
        print("Executando rotina 0029.")
        Ctrl.routine0029
        time.sleep(2) 