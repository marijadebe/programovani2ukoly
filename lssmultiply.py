class Vrchol:
    def __init__(self, hodnota: int, syn = None):
        self.hodnota = hodnota
        self.syn = syn

class LSS:
    def __init__(self, pocet: int = 1):
        self.hlava = Vrchol(1)
        ukazatel = self.hlava
        #Pro zkoušení kódu, vytvoření LSS s hodnotami 1,2,3,...,pocet
        for x in range(pocet):
            ukazatel.syn = Vrchol(x+1)
            ukazatel = ukazatel.syn
    
    def __str__(self):
        result = ""
        ukazatel = self.hlava.syn
        while ukazatel != None:
            result += str(ukazatel.hodnota)+" "
            ukazatel = ukazatel.syn
        return result
    
    def multiplyBy2(self):
        #Vytvoření ukazatele a opožděné ukazatele, prepisy je FIFO fronta se zarážkou
        ukazatel = self.hlava
        zarazka = 0
        prepisy = list()
        
        while ukazatel.syn != None:
            if len(prepisy) > 0 and ukazatel.hodnota <= prepisy[zarazka] <= ukazatel.syn.hodnota:
                novyVrchol = Vrchol(prepisy[zarazka], ukazatel.syn)
                ukazatel.syn = novyVrchol
                ukazatel = ukazatel.syn
                zarazka += 1
            if ukazatel.syn.hodnota % 5 == 0:
                prepisy.append(ukazatel.syn.hodnota*2)
                ukazatel.syn = ukazatel.syn.syn
            else:
                ukazatel = ukazatel.syn

        while len(prepisy[zarazka:]) > 0:
            ukazatel.syn = Vrchol(prepisy[zarazka], ukazatel.syn)
            zarazka += 1
            ukazatel = ukazatel.syn
        
velikost = int(input().strip())
seznam = LSS(velikost)
print(seznam)
seznam.multiplyBy2()
print(seznam)