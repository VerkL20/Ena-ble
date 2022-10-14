import random

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


print(nova_enacba)
print(int(eval(nova_enacba)))
