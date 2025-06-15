import random

class TURNIR ():

    def __init__ (self, naziv, *natjecatelji):
        self.naziv          = naziv
        self.natjecatelji   = natjecatelji
        self.kosare         = []
        self.podjela        = {}

        self.zapocni()
    
    
    # početna metoda jednog kruga natjecanja koja će rasčlaniti
    # košare u kojima se korisnici nalaze, zatražiti parove
    def zapocni (self):

        # pronalazak aktualnih vrsta košara
        for element in self.natjecatelji:
            if tuple(element.vrezultat) not in self.kosare:
                self.kosare.append(tuple(element.vrezultat))
        self.kosare.sort()

        # pripremam 
        for i in range (len(self.kosare)):
            self.podjela[i] = []
        
        for i in range (len(self.kosare)):
            for element in self.natjecatelji:
                if tuple(element.vrezultat) == self.kosare[i]:
                    self.podjela[i].append(element)
        
        print (self.kosare)
        for k, v in self.podjela.items():
            print(f'{k} -- {v}')
            
        print(self.vrati_parove(*self.natjecatelji))
    
    
    # metoda koja će za zadani popis natjecatelja vratiti parove; u ovom
    # slučaju to će biti nastumično povezani natjecatelji
    def vrati_parove (self, *natjecatelji):
        if len(natjecatelji)%2 != 0:
            print(f'Neću vratiti parove od neparnog broja igrača.')
            return None
        else:
            temp    = list(natjecatelji)    # touple ne mogu mješati
            parovi  = []                    # za vraćanje parova
            random.shuffle(temp)            
            for i in range (0, len(temp), 2):
                parovi.append((temp[i], temp[i+1]))
            return parovi

class NATJECATELJ ():
    brojnatjecatelja = 0
    
    def __init__ (self, ime, tezina):
        self.ime		= str(ime)
        self.tezina		= int(tezina)
        self.rezultat	= [0, 0]	# podatci o rezultatima
        
        NATJECATELJ.brojnatjecatelja += 1
    
    # metode za postavljanje vrijednosti
    def pime (self, tekstimena):
        self.ime = tekstimena
    def ptezinu (self, vrijednost):
        self.tezina = vrijednost
    def prezultat (self, *args):
        if args == []:
            self.rezultat = [0, 0]
        else:
            for i in range (2):
                self.rezultat[i] = args[i]
    
    @property
    def pobjeda (self):
        self.rezultat[0] += 1
    @property
    def gubitak (self):
        self.rezultat[1] += 1
    
    # metode za vraćanje podataka
    @property
    def vtezinu (self):
        return self.tezina
    @property
    def vrezultat (self):
        return self.rezultat
    @property
    def vpobjede (self):
        return self.rezultat[0]
    @property
    def vgubitke (self):
        return self.rezultat[1]
    
    def __str__ (self):
        return f'{self.ime}'
    def __repr__ (self):
        return f'#{self.tezina}_{self.ime}'
    
    def __del__ (self):
        NATJECATELJ.brojnatjecatelja -= 1


imena = ['Mario', 'Ivan', 'Antea', 'Roko', 'Marina', 'Sabka', 'Stjepan', 'Ana']
natjecatelj = []

for i in range (len(imena)): natjecatelj.append(NATJECATELJ(imena[i], 0))

print("-"*40)
print(natjecatelj)

# meč u kojem je 1 pobijedio 3
natjecatelj[0].pobjeda
natjecatelj[1].gubitak

# meč u kojem je 1 pobijedio 5
natjecatelj[3].pobjeda
natjecatelj[2].gubitak

print("-"*40)
print(f'\t\tPob\tGub')
print(f'\t\t-\t-')
for i in range(len(imena)):
    print(f'{natjecatelj[i]}\t\t{natjecatelj[i].vpobjede}\t{natjecatelj[i].vgubitke}')


t1 = TURNIR("glavni", *natjecatelj)

