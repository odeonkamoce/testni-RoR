# jednostruko vezana lista

class Element:
    
    def __init__ (self, podatak=None):
        self.prijasnji = None
        self.podatak = podatak
        
class VezanaLista:
    count = 0
    
    def __init__ (self):
        self.zadnji = None
    
    def dodaj(self, podatak):
        novi = Element(podatak)
        novi.prijasnji = self.zadnji
        self.zadnji = novi
        VezanaLista.count += 1
    
    def ispisi(self):
        e = self.zadnji
        while e:
            print(f'{e.podatak}')
            e = e.prijasnji
    
    def brisi (self, indeks):
        if indeks < 1 or indeks > VezanaLista.count:
            print("Nema traženog indeksa.")
            return
        if indeks == VezanaLista.count:
            self.zadnji = self.zadnji.prijasnji
            return
        trenutni_indeks = VezanaLista.count - 1
        cur_node = self.zadnji
        while cur_node:
            cvor_ispred = cur_node
            cur_node=cur_node.prijasnji
            if trenutni_indeks == indeks:
                cvor_ispred.prijasnji = cur_node.prijasnji
                VezanaLista.count -= 1
                return
            trenutni_indeks -=1
    
    def brisiVrijednost(self, vrijednost):
        cur_node = self.zadnji
        if cur_node.podatak == vrijednost:
            self.zadnji = self.zadnji.prijasnji
            return
        while cur_node.prijasnji:
            prethodni_cvor = cur_node
            cur_node = cur_node.prijasnji
            if cur_node.podatak == vrijednost:
                prethodni_cvor.prijasnji = cur_node.prijasnji
    
    def obrisi_cijelu_listu(self):
        self.zadnji = None
        VezanaLista.count = 0
        
    def dodaj_na_pocetak(self, podatak):
        novi = Element(podatak)
        if self.zadnji == None:
            self.zadnji = novi
        else:
            cur_node = self.zadnji
            while cur_node.prijasnji:
                cur_node = cur_node.prijasnji
            cur_node.prijasnji = novi
            VezanaLista.count += 1
    
    def umetni (self, podatak, indeks):
        novi = Element(podatak)
        if indeks < 1 or indeks > VezanaLista.count:
            print("Nema traženog indeksa.")
            return
        if indeks == VezanaLista.count:
            self.dodaj(podatak)
            return
        trenutni_indeks = VezanaLista.count - 1
        cur_node = self.zadnji
        while cur_node.prijasnji:
            cvor_ispred = cur_node
            cur_node = cur_node.prijasnji
            if trenutni_indeks == indeks:
                cvor_ispred.prijasnji = novi
                novi.prijasnji = cur_node
                VezanaLista.count += 1
            trenutni_indeks -= 1
    
    def okreni (self):
        prethodni = None
        cur_node = self.zadnji
        while cur_node:
            # 6
            slijedeci = cur_node.prijasnji
            
            cur_node.prijasnji = prethodni
            
            prethodni = cur_node
            
            cur_node = slijedeci
        self.zadnji = prethodni
    
    def u_niz(self):
        cur_node = self.zadnji
        niz = []
        while cur_node:
            niz.append(cur_node.podatak)
            cur_node = cur_node.prijasnji
        return niz
    
    def sortiraj(self):
        elementi = self.u_niz()
        elementi.sort()
        self.obrisi_cijelu_listu()
        for element in elementi:
            self.dodaj(element)
    
    
        

lista = VezanaLista()
lista.dodaj("1 jedan")
lista.dodaj("2 dva")
lista.dodaj("3 tri")
lista.dodaj("4 četiri")
lista.dodaj("5 pet")
lista.dodaj("6 šest")
lista.dodaj("7 sedam")

lista.ispisi()

# print("--------------------------")
# lista.brisi(5)
# lista.ispisi()

# print("--------------------------")
# lista.brisiVrijednost("4 četiri")
# lista.ispisi()

# print("--------------------------")
# lista.dodaj_na_pocetak("0 nula")
# lista.ispisi()

# print("--------------------------")
# lista.umetni("X iks", 5)
# lista.ispisi()

print("----------------------")
lista.okreni()
lista.ispisi()

print(lista.u_niz())

print("-------------------------")
lista.sortiraj()

lista.ispisi()


"""    
d1 = Element("pon")
d2 = Element("uto")
d3 = Element("sri")
d4 = Element("čet")
d5 = Element("pet")

d2.prijasnji = d1
d3.prijasnji = d2
d4.prijasnji = d3
d5.prijasnji = d4

thisValue = d5

while thisValue:
    print(thisValue.podatak)
    thisValue = thisValue.prijasnji
"""
