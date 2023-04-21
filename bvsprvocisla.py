from math import isqrt

def jePrvocislo(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    strop = isqrt(n)
    for i in range(5, strop+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

class Leaf:
    def __init__(self, hodnota: int, levySyn = None, pravySyn = None):
        self.hodnota = hodnota
        self.levySyn = levySyn
        self.pravySyn = pravySyn
    def __setitem__(self, klic, hodnota):
        match klic:
            case 0: self.levySyn = hodnota
            case 1: self.pravySyn = hodnota
    def __getitem__(self, klic):
        match klic:
            case 0: return self.levySyn
            case 1: return self.pravySyn

class BVS:
    def __init__(self, rozpeti: int):
        self.koren = self.zaplnStrom(list(range(1, rozpeti+1)), 0, rozpeti-1)
        self.najdiOdstranPrvocisla()
        BVS.printStrom(self.koren)

    @staticmethod
    def printStrom(leaf: Leaf, level: int = 0):
        if leaf != None:
            BVS.printStrom(leaf.levySyn, level + 1)
            print(' ' * 4 * level + '-> ' + str(leaf.hodnota))
            BVS.printStrom(leaf.pravySyn, level + 1)
    
    def zaplnStrom(self, seznam: list, leva: int, prava: int) -> Leaf:
        if leva > prava: return None
        mid = (leva + prava) // 2
        listecek = Leaf(seznam[mid])
        listecek.levySyn = self.zaplnStrom(seznam, leva, mid-1)
        listecek.pravySyn = self.zaplnStrom(seznam, mid+1, prava)
        return listecek
    
    def _najdiOdstranMinimum(self, strom: Leaf) -> int:
        minimum = 0
        if strom.levySyn == None:
            minimum = strom.hodnota
        elif strom.levySyn.levySyn == None:
            minimum = strom.levySyn.hodnota
            if strom.levySyn.pravySyn == None:
                strom.levySyn = None
            else:
                strom.levySyn = strom.levySyn.pravySyn
        else:
            minimum = self._najdiOdstranMinimum(strom.levySyn)
        return minimum

    def najdiOdstranPrvocisla(self):
        self.koren = Leaf(1, self.koren)
        self._najdiOdstranPrvocisla(self.koren)
        self.koren = self.koren.levySyn

    def _najdiOdstranPrvocisla(self, strom: Leaf):
        #Proveď to stejné pro pravého a levého syna.
        for x in {0,1}:
            #while je tady, jelikož se může na původní hladinu procesem mazání se dvěma syny dostat znovu prvočíslo
            while strom[x] != None and jePrvocislo(strom[x].hodnota):
                if strom[x].pravySyn == strom[x].levySyn == None:
                    strom[x] = None
                elif strom[x].levySyn != None and strom[x].pravySyn == None:
                    strom[x] = strom[x].levySyn
                elif strom[x].pravySyn != None and strom[x].levySyn == None:
                    strom[x] = strom[x].pravySyn
                else:
                    strom[x].hodnota = self._najdiOdstranMinimum(strom[x].pravySyn)
                    #_najdiOdstranPrvocisla ukazuje na syna, pokud je syn prázdný, tak ho neodstraní - to zařídím tady
                    if strom[x].pravySyn.hodnota == strom[x].hodnota: strom[x].pravySyn = strom[x].pravySyn.pravySyn

            if strom[x] != None: self._najdiOdstranPrvocisla(strom[x])

strom = BVS(int(input().strip()))