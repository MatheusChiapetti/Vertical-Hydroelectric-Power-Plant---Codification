from colorama import init, Fore, Back, Style
from datetime import datetime
import random as random
import math as math
import time as time
import sys as sys

class Ctrl:
    
    def routine0022():
        print(f"{Fore.YELLOW}{Back.BLACK}As comportas estão sendo abertas.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}As comportas foram totalmente abertas.{Fore.RESET}{Back.RESET}")
    
    def routine0023():
        print(f"{Fore.YELLOW}{Back.BLACK}As comportas estão sendo fechadas.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}As comportas foram totalmente fechadas.{Fore.RESET}{Back.RESET}")
        print()
    
    def routine0024(alpha):
        if(alpha == 30):
            print(f"{Fore.RED}{Back.BLACK}O ângulo a é máximo e o ajuste não pode ser feito.{Fore.RESET}{Back.RESET}")
            print()
        print(f"{Fore.YELLOW}{Back.BLACK}As pás de captação estão sendo abertas.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}As pás de captação foram ajustadas.{Fore.RESET}{Back.RESET}")
        print()
        alpha = alpha + 1
        return alpha
    
    def routine0025(alpha):
        if(alpha == 0):
            print(f"{Fore.RED}{Back.BLACK}O ângulo a é mínimo e o ajuste não pode ser feito.{Fore.RESET}{Back.RESET}")
            print()
        elif(0 < alpha <= 30):
            print(f"{Fore.YELLOW}{Back.BLACK}As pás de captação estão sendo fechadas.{Fore.RESET}{Back.RESET}")
            time.sleep(2)
            print(f"{Fore.GREEN}{Back.BLACK}As pás de captação foram ajustadas.{Fore.RESET}{Back.RESET}")
            print()
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
        print(f"{Fore.YELLOW}{Back.BLACK}As pás de distribuição das turbinas estão sendo abertas.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}As pás de distribuição das turbinas foram abertas.{Fore.RESET}{Back.RESET}")
        print()
    
    def routine0028():
        print(f"{Fore.YELLOW}{Back.BLACK}As pás de distribuição das turbinas estão sendo fechadas.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}As pás de distribuição das turbinas foram fechadas.{Fore.RESET}{Back.RESET}")
        print()
    
    def routine0029():
        print(f"{Fore.YELLOW}{Back.BLACK}Aciondando sistemas de drenagem.{Fore.RESET}{Back.RESET}")
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}A água foi drenada dos condutos")
        print()
    
    def routine0030():
        data_atual = datetime.now()
        print(f"Não há nenhuma manutenção agendada para {data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}.{Fore.RESET}{Back.RESET}")
    
    def routine0031(alpha):
        print(f"{Fore.YELLOW}{Back.BLACK}A usina será inicializada.{Fore.RESET}{Back.RESET}")
        Ctrl.routine0022()
        Ctrl.routine0025(alpha)
        time.sleep(2)
        Ctrl.routine0027()
        time.sleep(2)
        print(f"{Fore.GREEN}{Back.BLACK}A usina foi inicializada.{Fore.RESET}{Back.RESET}")
    
    def routine0032(alpha):
        print()
        print(f"{Fore.YELLOW}{Back.RED}==> A usina será desligada. <== {Fore.RESET}{Back.RESET}")
        print()
        print(f"{Fore.YELLOW}{Back.WHITE}Executando rotina 0025.{Fore.RESET}{Back.RESET}")
        Ctrl.routine0025(alpha)
        time.sleep(2)
        print(f"{Fore.YELLOW}{Back.WHITE}Executando rotina 0028.{Fore.RESET}{Back.RESET}")
        Ctrl.routine0028()
        time.sleep(2)
        print(f"{Fore.YELLOW}{Back.WHITE}Executando rotina 0023.{Fore.RESET}{Back.RESET}")
        Ctrl.routine0023()
        time.sleep(2)
        print(f"{Fore.YELLOW}{Back.WHITE}Executando rotina 0029.{Fore.RESET}{Back.RESET}")
        Ctrl.routine0029()
        time.sleep(2) 
        sys.exit()