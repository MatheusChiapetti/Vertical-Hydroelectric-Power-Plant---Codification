import random as random
import math as math
import time as time

class PyTie:

    '''
    As fórmulas escolhidas para serem codificadas foram: força contra uma superfície plana (1.2); potência da turbina (1.6); carga manométrica da turbina (1.7); equação de Bernoulli (1.8); perda de carga distribuída (1.13); perda de carga singular (1.15); aumento proporcional x (2.1); diâmetro de abertura (2.2); altura da queda d'água (2.3); vazão volumétrica no ponto 1 (2.4); vazão volumétrica no ponto 2 (2.5); vazão volumétrica no ponto 3 (2.6); vazão volumétrica no ponto 4 (2.7); conta do ponto 1 (2.8); cota no ponto 2 (2.9); cota no ponto 3 (2.10); cota no ponto 4 (2.11); cota no ponto 5 (2.12); comprimento do conduto (2.13); velocidade média entre os pontos 1 e 2 (2.15); velocidade média entre os pontos 2 e 3 (2.16); e velocidade média entre os pontos 3 e 4 (2.17). Por meio das fórmulas da vazão volumétrica, seguindo o princípio da equação da continuidade, é possível descobrir a velocidade nos pontos. '''

    # Força contra uma superfície plana.
    def equad01(y, z5):
        P = y * z5
        return P
    
    # Potência da turbina.
    def equad02(Q, nt, p, hq):
        Pw = Q * nt * p * hq * (9.81/1000)
        return Pw

    # Carga manométrica da turbina.
    def equad03(Pw, y, Q, nt):
        Ht = Pw / (y * nt * Q)
        return Ht

    # Equação de Bernoulli (Encontrar Carga Total).
    def equad04(z, v, g, y, P):
        gg = 2 * g
        v_2 = round(((math.pow(v,2)) / gg))
        P_y = round((P / y), 2)
        H = z + v_2 + P_y
        return round(H, 2)
    
    # Equação de Bernoulli (Encontrar Pressão).
    def equad05(H, z, v, g, y):
        gg = 2 * g
        v_2 = round(((math.pow(v,2))/ gg))
        P = (H - v_2 - z) * y
        return P

    # Perda de carga distribuída.
    def equad06(f, L, Dh, vm, g):
        hf = f * (L/Dh) * ((math.pow(vm,2)/ 2 * g))
        return hf

    # Perda de carga singular. 
    def equad07(ks, vm, g):
        hs = ks * ((math.pow(vm,2)/ 2 * g)) 
        return hs
    
    # Diâmetro de abertura.
    def equad08(alpha):
        if(alpha == 30):
            da = 24
        elif(alpha == 25):
            da = 22.08
        elif(alpha == 21):
            da = 20.4
        elif(alpha == 18):
            da = 19.2
        elif(alpha == 15):
            da = 18
        elif(alpha == 12):
            da = 16.8
        elif(alpha == 10):
            da = 16.08
        elif(alpha == 8):
            da = 15.12
        elif(alpha == 5):
            da = 13.92
        elif(alpha == 0):
            da = 0        
        return da
    
    # Altura da queda d'água. 
    def equad09(hc, de, hd):
        hq = hc + de + hd
        return hq

    # Vazão volumétrica no ponto 1.
    def equad10(da, de, hc, vf):
        Qf = ((de + hc) * da) * vf
        return Qf

    # Vazão volumétrica no ponto 2 (Velocidade 2).
    def equad11(de, pi, Qf):
        v = (math.pow(de/2, 2) * pi)
        v2 = Qf / (v)
        return v2

    # Vazão volumétrica no ponto 3 (Velocidade 3).
    def equad12(dt, pi, Qf):
        v = (math.pow(dt/2, 2) * pi)
        v3 = Qf / (v)
        return v3
    
    # Vazão volumétrica no ponto 4 (Velocidade 4).
    def equad13(ds, pi, Qf):
        v = (math.pow(ds/2, 2) * pi)
        v4 = Qf / (v)
        return v4

    # Velocidade média entre os pontos 1 e 2.
    def equad14(vf, v2):
        vm1_2 = (vf + v2) / 2
        return vm1_2
    
    # Velocidade média entre os pontos 2 e 3.
    def equad15(v2, v3):
        vm2_3 = (v2 + v3) / 2
        return vm2_3
    
    # Velocidade média entre os pontos 3 e 4.
    def equad16(v3, v4):
        vm3_4 = (v3 + v4) / 2
        return vm3_4
    
    # Cota no ponto 1.
    def equad17(de, hc, hd, hr):
        z1 = de + hc + hd + hr
        return z1

    # Cota no ponto 2.
    def equad18(de, hd, hr):
        z2 = (de/2) + hd + hr
        return z2
    
    # Cota no ponto 3.
    def equad19(dt, hr):
        z3 = (dt/2) + hr
        return z3
    
    # Cota no ponto 4.
    def equad20(hr, dt):
        z4 = hr - (dt/2)
        return z4
    
    # Cota no ponto 5.
    def equad21(ds, hq):
        z5 = (ds/2) + hq
        return z5
    
    # Comprimento do conduto forçado.
    def equad22(hd, de, sec):
        L = (hd + de) * sec
        return L

    




