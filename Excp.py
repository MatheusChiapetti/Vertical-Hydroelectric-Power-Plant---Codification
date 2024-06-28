from colorama import init, Fore, Back, Style
from datetime import datetime
import random as random
from Ctrl import Ctrl
import math as math
import time as time

class Excp: 
    init()       
    
    r1 = "enviar uma equipe de manutenção para o local imediatamente"
    r2 = "realizar verificações adicionais para melhor avaliar os danos"
    r3 = "manter a usina desligada"
    r4 = "verificar se todos os funcionários saíram da usina e não sofreram ferimentos"
    r5 = "enviar uma equipe para restabelecer a conexão elétrica"
    r6 = "avaliar possíveis danos aos equipamentos e à estrutura de modo mais detalhado"
    r7 = "verificar a integridade do conjunto turbina + eixo + rotor"
    r8 = "entrar em contato com os serviços de emergência, incluindo bombeiros"
    r9 = "cortar a energia elétrica da usina para prevenir curtos-circuitos e novos focos de incêndio"
    r10 = "verificar se todos os funcionários saíram da usina e não sofreram ferimentos ou queimaduras"
    r11 = "desligar a usina caso os danos sejam significativos ou prejudiquem o funcionamento normal da estrutura"
    r12 = "verificar se nenhum funcionário foi ferido no acidente"
    r13 = "iniciar os consertos necessários e substituir o cabo"
    r14 = "avaliar se houve danos ao meio ambiente"
    r15 = "informar as autoridades responsáveis sobre o acidente" 
    r16 = "iniciar os consertos necessários e substituir as pás de captação"
    r17 = "iniciar os consertos necessários e substituir o conjunto turbina + eixo + rotor"

    def routine0033():
        data_atual = datetime.now()
        print(f"{Back.RED}{Fore.BLACK}==> Evacuar imediatamente a usina! <=={Fore.RESET}{Back.RESET}")
        print()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu o rompimento do conduto forçado da usina, levando ao alagamento de diversas áreas.")
        print()
    
    def routine0034():
        estado = random.randint(0, 1)
        return estado
    
    def routine0035():
        data_atual = datetime.now()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, um corpo estranho entrou nos condutos da usina.")
        print()
    
    def routine0036():
        data_atual = datetime.now()
        print(f"{Back.RED}{Fore.BLACK}==> Evacuar imediatamente a usina! <=={Fore.RESET}{Back.RESET}")
        print()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu o rompimento do casco da usina, levando ao alagamento de diversas áreas.")
        print()

    def routine0037():
        data_atual = datetime.now()
        print(f"{Back.RED}{Fore.BLACK}==> Evacuar imediatamente a usina! <=={Fore.RESET}{Back.RESET}")
        print()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu um foco de incêndio na usina.")
        print()
    
    def routine0038():
        data_atual = datetime.now()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu uma falha no sistema de drenagem.")
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} mesmo com a falha no sistema de drenagem, não ocorreram danos consideráveis à usina.")
        print()

    def routine0039(alpha):
        Ctrl.routine0032(alpha)
        print(f"{Fore.BLUE} ==> {Fore.RESET}Devido ao clima severo (Tempestade), a usina foi desligada.{Fore.BLUE} <== {Fore.RESET}")
        print()
    
    def routine0040():
        data_atual = datetime.now()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu na lateral, próxima às pás de captação, uma colisão contra o casco da usina")
        print()
    
    def routine0041():
        data_atual = datetime.now()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu o rompimento do cabo de trasmissão de energia.")
        print()
    
    def routine0042():
        data_atual = datetime.now()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu o desmembramento de uma das pás de captação.")
        print()
    
    def routine0043():
        data_atual = datetime.now()
        print(f"{Back.RED}{Fore.BLACK}==> Evacuar imediatamente a usina! <=={Fore.RESET}{Back.RESET}")
        print()
        print(f"No dia {Fore.BLUE}{data_atual.strftime("%d/%m/%Y, as %H:%M:%S")}{Fore.RESET}, ocorreu o descontrole do conjunto (turbina + eixo + rotor).")
        print()
 
    def routine0044():
        Ctrl.routine0023()
        time.sleep(2)
        Ctrl.routine0028()
        time.sleep(2)
        Ctrl.routine0029() 
        time.sleep(2)
        print(f"{Fore.BLUE}{Back.BLACK}A transmissão de energia foi interrompida.{Back.RESET}{Fore.RESET}")
        print()
        print(f"{Fore.WHITE}{Back.RED}A usina foi desligada.{Fore.RESET}{Back.RESET}")

    def routine0045(alpha):
        Ctrl.routine0032(alpha)
        print(f"{Fore.BLUE} ==> {Fore.RESET} Ocorreu a estagnação da água nos condutos da usina.{Fore.BLUE} <== {Fore.RESET}")
        print()
        print(f"{Back.BLACK}Danos:{Back.RESET} não ocorreram danos significativos à estrutura ou às tubulações.")


