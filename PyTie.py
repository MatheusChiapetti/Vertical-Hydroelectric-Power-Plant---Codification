import random as random
import math as math
import time as time

class PyTie:

    '''
    As fórmulas escolhidas para serem codificadas foram: força contra uma superfície plana (1.2); potência da turbina (1.6); carga manométrica da turbina (1.7); equação de Bernoulli (1.8); perda de carga distribuída (1.13); perda de carga singular (1.15); aumento proporcional x (2.1); diâmetro de abertura (2.2); altura da queda d'água (2.3); vazão volumétrica no ponto 1 (2.4); vazão volumétrica no ponto 2 (2.5); vazão volumétrica no ponto 3 (2.6); vazão volumétrica no ponto 4 (2.7); conta do ponto 1 (2.8); cota no ponto 2 (2.9); cota no ponto 3 (2.10); cota no ponto 4 (2.11); cota no ponto 5 (2.12); comprimento do conduto (2.13); velocidade média entre os pontos 1 e 2 (2.15); velocidade média entre os pontos 2 e 3 (2.16); e velocidade média entre os pontos 3 e 4 (2.17). Por meio das fórmulas da vazão volumétrica, seguindo o princípio da equação da continuidade, é possível descobrir a velocidade nos pontos. '''

    # Força contra uma superfície plana.

    # Potência da turbina.

    # Carga manométrica da turbina.

    # Equação de Bernoulli.

    # Perda de carga distribuída.

    # Perda de carga singular. 

    # Diâmetro de abertura.
    def equad07(de, alpha, cl):
        x = math.sin(alpha) * cl
        da = de + (2 * x)
        return da
    
    # Altura da queda d'água. 
    def equad08(hc, de, hd):
        hq = hc + de + hd
        return hq

    # Vazão volumétrica no ponto 1.
    def equad09(da, de, hc, vf):
        Qf = (da * (de + hc)) * vf
        return Qf

    # Vazão volumétrica no ponto 2 (Velocidade 2).
    def equad10(de, pi, Qf):
        v2 = Qf / (math.pow(de, 2) * pi)
        return v2

    # Vazão volumétrica no ponto 3 (Velocidade 3).
    def equad11(dt, pi, Qf):
        v3 = Qf / (math.pow(dt, 2) * pi)
        return v3
    
    # Vazão volumétrica no ponto 4 (Velocidade 4).
    def equad12(ds, pi, Qf):
        v4 = Qf / (math.pow(ds, 2) * pi)
        return v4

    # Velocidade média entre os pontos 1 e 2.

    # Velocidade média entre os pontos 2 e 3.

    # Velocidade média entre os pontos 3 e 4.

    # Cota no ponto 1.

    # Cota no ponto 2.

    # Cota no ponto 3.

    # Cota no ponto 4.

    # Cota no ponto 5.

    # Comprimento do conduto forçado.

    




