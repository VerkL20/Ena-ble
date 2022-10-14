import random
import json

STEVILO_DOVOLJENIH_POSKUSOV = 6
ZNAK = 'Z'
UGIB = 'U'
PRAVILNE_STEVKE = 'PS'
PRAVILNE_OPERACIJE = 'PO'
START = 'S'
ZMAGA = 'W'
PORAZ = 'X'
NAPACEN_UGIB = 'NU'

DATOTEKA_S_STANJEM = 'datoteka_s_stanjem.json'
REGULARNI_UGIBI = []

class Igra():
    def __init__(self, enacba, ugibi=None):
        self.enacba = enacba
        if ugibi == None:
            self.ugibi = []
        else:
            self.ugibi = ugibi
        
    def rezultat(self):
        return int(eval(self.enacba))

    def regularen_ugib(self, ugib):
        operacije = ['+', '-', '*', '/']
        stevke = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(ugib) != 6:
            return False
        elif ugib[0] in operacije or ugib[-1] in operacije:
            return False
        elif ugib[0] == '0' and ugib[1] in stevke:
            return False
        else:
            for i in range(len(ugib)):
                if ugib[i] not in stevke and ugib[i] not in operacije:
                    return False
                elif ugib[i] in operacije and ugib[i-1] in operacije:
                    return False
                elif i != 5 and ugib[i] == '0' and ugib[i-1] in operacije and ugib[i+1] in stevke:
                    return False
                elif int(eval(ugib)) != self.rezultat():
                    return False
        return True

    def st_pravilnih_znakov(self, ugib):
        operacije = ['+', '-', '*', '/']
        PO = 0
        PS = 0
        zacasna_enacba = [*self.enacba]
        for znak in ugib:
            if znak in zacasna_enacba:
                if znak in operacije:
                    PO += 1
                else:
                    PS += 1
                zacasna_enacba.remove(znak)
        return (PO, PS)


    def zmaga(self):
        ugib = self.ugibi[-1]
        zacasna_enacba = [*self.enacba]
        for znak in ugib:
            if znak not in zacasna_enacba:
                return False
            zacasna_enacba.remove(znak)
        return True
    
    def stevilo_poskusov(self):
        return len(self.ugibi)

    def poraz(self):
        return len(REGULARNI_UGIBI) > STEVILO_DOVOLJENIH_POSKUSOV

    def ugibanje(self, ugib):
        self.ugibi.append(ugib)
        if self.regularen_ugib(ugib):
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            else:
                (operacije, stevke) = self.st_pravilnih_znakov(ugib)
                REGULARNI_UGIBI.append([ugib, operacije, stevke])
                return REGULARNI_UGIBI
        return False





def nova_igra():
    operacije = ['+', '-', '*', '/']
    stevke = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    stevke_brez_nic = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mozne_postavitve_operacij = [(1,3), (1,4), (2,4)]
    nova_enacba = []
    nova_enacba.append(random.choice(stevke_brez_nic))
    nova_enacba.append(random.choice(stevke))
    nova_enacba.append(random.choice(stevke))
    nova_enacba.append(random.choice(stevke))

    if 0 not in nova_enacba:
        postavitve_operacij = random.choice(mozne_postavitve_operacij)
        izbrane_operacije = random.choice(operacije)
        if '/' != izbrane_operacije:
            nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
        elif '/' == izbrane_operacije and postavitve_operacij == (1,4):
            while postavitve_operacij == (1,4):
                postavitve_operacij = random.choice(mozne_postavitve_operacij)

        if '/' == izbrane_operacije and postavitve_operacij == (1,3):
            while nova_enacba[0] % nova_enacba[1] != 0:
                nova_enacba[0] = random.choice(stevke_brez_nic)
                nova_enacba[1] = random.choice(stevke_brez_nic)
            nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
        elif '/' == izbrane_operacije and postavitve_operacij == (2,4):
            while (nova_enacba[0] * 10 + nova_enacba[1]) % nova_enacba[2] != 0:
                nova_enacba[0] = random.choice(stevke_brez_nic)
                nova_enacba[1] = random.choice(stevke_brez_nic)
                nova_enacba[2] = random.choice(stevke_brez_nic)
            nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
        

        izbrane_operacije = random.choice(operacije)
        if '/' != izbrane_operacije:
            nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            
        elif '/' == izbrane_operacije and '*' not in nova_enacba and '/' not in nova_enacba:
            if postavitve_operacij == (1,3):
                postavitve_operacij = (1,4)

            if postavitve_operacij == (1,4):
                while (nova_enacba[2] * 10 + nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
            elif postavitve_operacij == (2,4):
                while nova_enacba[3] % nova_enacba[4] != 0:
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
        elif '/' == izbrane_operacije and '*' in nova_enacba:
            if postavitve_operacij == (1,3):
                while (nova_enacba[0] * nova_enacba[2]) % (nova_enacba[3] * 10 + nova_enacba[4]) != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
            elif postavitve_operacij == (1,4):
                while (nova_enacba[0] * (nova_enacba[2] * 10 + nova_enacba[3])) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
            elif postavitve_operacij == (2,4):
                while ((nova_enacba[0] * 10 + nova_enacba[1]) * nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[1] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
            
        elif '/' == izbrane_operacije and '/' in nova_enacba:
            if postavitve_operacij == (1,3):
                while izbrane_operacije == '/':
                    izbrane_operacije = random.choice(operacije)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                
            elif postavitve_operacij == (2,4):
                while ((nova_enacba[0] * 10 + nova_enacba[1]) / nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[1] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
                

    elif 0 in nova_enacba:
        izbrane_operacije = random.choice(operacije)
        while nova_enacba.count(0) != 1:
            nova_enacba[1] = random.choice(stevke)
            nova_enacba[2] = random.choice(stevke)
            nova_enacba[3] = random.choice(stevke)
        
        if nova_enacba[1] == 0:
            postavitve_operacij = (2,4)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and postavitve_operacij == (2,4):
                while (nova_enacba[0] * 10) % nova_enacba[2] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
            
            izbrane_operacije = random.choice(operacije)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' not in nova_enacba and '/' not in nova_enacba:
                    while nova_enacba[3] % nova_enacba[4] != 0:
                        nova_enacba[3] = random.choice(stevke_brez_nic)
                        nova_enacba[4] = random.choice(stevke_brez_nic)
                    nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' in nova_enacba:
                while (nova_enacba[0] * 10  * nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '/' in nova_enacba:
                while ((nova_enacba[0] * 10) / nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            
            
        elif nova_enacba[2] == 0:
            postavitve_operacij = (1,4)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije:
                while '/' == izbrane_operacije:
                    izbrane_operacije = random.choice(operacije)
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
            
            izbrane_operacije = random.choice(operacije)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' not in nova_enacba:    
                while (nova_enacba[2] * 10 + nova_enacba[3]) % nova_enacba[4] != 0:
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' in nova_enacba:
                while (nova_enacba[0] * (nova_enacba[2] * 10 + nova_enacba[3])) % nova_enacba[4] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[4] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]

        elif nova_enacba[3] == 0:
            postavitve_operacij = (1,3)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije:
                while nova_enacba[0] % nova_enacba[1] != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[1] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[0]:postavitve_operacij[0]] = izbrane_operacije[0]

            izbrane_operacije = random.choice(operacije)
            if '/' != izbrane_operacije:
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' not in nova_enacba:
                while izbrane_operacije == '/':
                    izbrane_operacije = random.choice(operacije)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            elif '/' == izbrane_operacije and '*' in nova_enacba:
                while (nova_enacba[0] * nova_enacba[2]) % (nova_enacba[3] * 10) != 0:
                    nova_enacba[0] = random.choice(stevke_brez_nic)
                    nova_enacba[2] = random.choice(stevke_brez_nic)
                    nova_enacba[3] = random.choice(stevke_brez_nic)
                nova_enacba[postavitve_operacij[1]:postavitve_operacij[1]] = izbrane_operacije[0]
            
    nova_enacba = ''.join(str(znak) for znak in nova_enacba)

    return Igra(nova_enacba)

class Iskanje_enacbe():
    def __init__(self):
        self.igre = {}
        self.datoteka_s_stanjem = 'datoteka_s_stanjem.json'
    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        enacba = nova_igra()
        self.nalozi()
        #igra = Igra(enacba, [])
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (enacba, START)
        self.shrani()
        return id_igre

    def ugibaj(self, id_igre, ugib):
        self.nalozi()
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibanje(ugib)
        self.igre[id_igre] = (igra, stanje)
        self.shrani()

    def shrani(self):
        with open(self.datoteka_s_stanjem, 'w') as f:
            igre = {id_igre: ((igra.enacba, igra.ugibi), stanje) for (id_igre, (igra, stanje)) in self.igre.items()}
            json.dump(igre, f)

    def nalozi(self):
        with open(self.datoteka_s_stanjem, 'r') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(enacba, ugibi), stanje) for (id_igre, ((enacba, ugibi), stanje)) in igre.items()}
        
    


        
