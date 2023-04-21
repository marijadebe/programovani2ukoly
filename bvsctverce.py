import math
class Vrchol:
    def __init__(self, hodnota: int, syn = None):
        self.hodnota = hodnota
        self.syn = syn

    def __str__(self):
        return str(self.hodnota) if self.syn == None else str(self.hodnota)+", "+str(self.syn)

class Leaf:
    def __init__(self, hodnota: int, levySyn = None, pravySyn = None):
        self.hodnota = hodnota
        self.levySyn = levySyn
        self.pravySyn = pravySyn
    
class BVS:
    def __init__(self, rozpeti: int):
        self.koren = self.zaplnStrom(list(range(1, rozpeti+1)), 0, rozpeti-1)
        print(self.najdiCtverce(self.koren).syn)

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
    
    #Vraci None, pokud nenalezl ctverce, jinak vraci LSS ctvercu
    def najdiCtverce(self, stromecek: Leaf) -> Vrchol | None:
        spojovySeznam = Vrchol(-1)
        ukazatel = spojovySeznam
        def jeCisloCtverec(hodnota: int) -> bool:
            return math.isqrt(hodnota)**2 == hodnota
        def inorderSpojak(stromecek: Leaf):
            nonlocal ukazatel
            if stromecek.levySyn != None:
                inorderSpojak(stromecek.levySyn)
            if jeCisloCtverec(stromecek.hodnota):
                ukazatel.syn = Vrchol(stromecek.hodnota)
                ukazatel = ukazatel.syn
            if stromecek.pravySyn != None:
                inorderSpojak(stromecek.pravySyn)
        inorderSpojak(stromecek)
        return spojovySeznam

strom = BVS(25)