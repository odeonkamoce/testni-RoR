import random

class TURNIR ():

    def __init__ (self, naziv, *natjecatelji):
        self.naziv              = naziv
        self.natjecatelji       = natjecatelji
        self.skupine            = []
        self.clanovi_skupina    = {}

        self.zapocni()
    
    
    # početna metoda jednog kruga natjecanja koja će rasčlaniti
    # košare u kojima se sudionici nalaze, zatražiti parove
    def zapocni (self):

        self.podjeli_na_skupine()
        self.ispis_po_skupinama()
            
        print(self.vrati_parove(*self.natjecatelji))
        
        for i in range (len(self.clanovi_skupina)):
            print(f'\n')
            print(f'Molim odabrati pobjednika 1 ili 2 u skupini {self.skupine[i]}:')
            parovi = self.vrati_parove(*self.clanovi_skupina[i])
            
            for element in parovi:                
                provjera_unosa_rezultata = False
                while not provjera_unosa_rezultata:
                    rezultat = int(input(f'{element[0]}\tprotiv\t{element[1]}\t= '))
                    if rezultat < 1 or rezultat > 2:
                        print (f'Neispravan unos, molim pokušajte ponovo.')
                    else:
                        element[rezultat-1].pobjeda
                        element[rezultat%2].gubitak
                        provjera_unosa_rezultata = True
        
        self.podjeli_na_skupine()
        self.ispis_po_skupinama()
    
    def unos_rezultata (self):
        for i in range (len(self.clanovi_skupina)):
            print(f'\n')
            print(f'Molim odabrati pobjednika 1 ili 2 u skupini {self.skupine[i]}:')
            parovi = self.vrati_parove(*self.clanovi_skupina[i])
            
            for element in parovi:                
                provjera_unosa_rezultata = False
                while not provjera_unosa_rezultata:
                    rezultat = int(input(f'{element[0]}\t-\t{element[1]}\t= '))
                    if rezultat < 1 or rezultat > 2:
                        print (f'Neispravan unos, molim pokušajte ponovo.')
                    else:
                        element[rezultat-1].pobjeda
                        element[rezultat%2].gubitak
                        provjera_unosa_rezultata = True
    
    def podjeli_na_skupine(self):
        # brišem stanje u varijablama
        self.skupine     = []
        self.clanovi_skupina    = {}
        
        # pronalazak aktualnih vrsta košara
        for element in self.natjecatelji:
            if tuple(element.vrezultat) not in self.skupine:
                self.skupine.append(tuple(element.vrezultat))
        self.skupine.sort()

        # priprema liste koja će sadržavati popise natjecatelja 
        for i in range (len(self.skupine)):
            self.clanovi_skupina[i] = []
        
        # za svaki tip košare koji imamo, popuniti listu
        # natjecatelja tako da odgovara po indeksu
        for i in range (len(self.skupine)):
            for element in self.natjecatelji:
                if tuple(element.vrezultat) == self.skupine[i]:
                    self.clanovi_skupina[i].append(element)


    # metoda koja će na ekran ispisati košare koje trenutno imamo
    # u natjecanju, te članove tih košara
    def ispis_po_skupinama (self):
        
        # pripremanje urednog ispisa popisa košara
        popis = ''          # početak s praznim stringom
        for element in self.skupine:
            popis += str(element) + ', '
        popis = popis[:-2]  # uklanjanje zadnjeg zareza
        
        print (f'\nTrenutno postoje košare {popis}:')
        for k, v in self.clanovi_skupina.items():
            print(f'{str(self.skupine[int(k)])} \t {v}')



    # metoda koja će za zadani popis natjecatelja vratiti parove; u ovom
    # slučaju to će biti nasumično povezani natjecatelji
    def vrati_parove (self, *natjecatelji):
        if len(natjecatelji)%2 != 0:
            print(f'Neću vratiti parove od neparnog broja igrača.')
            return None
        else:
            temp    = list(natjecatelji)    # tuple se ne može mijenjati
            parovi  = []                    # za vraćanje popisa parova
            
            ###     NASUMIČNO UPARIVANJE     ###
            random.shuffle(temp)
            
            # slaganje parova iz uređenog popisa temp
            for i in range (0, len(temp), 2):
                parovi.append((temp[i], temp[i+1]))
            
            # vraćanje popisa parova
            return parovi

class NATJECATELJ ():
    brojnatjecatelja = 0
    
    def __init__ (self, ime, tezina):
        self.ime		= str(ime)
        self.tezina		= int(tezina)
        self.rezultat	= [0, 0]	# podatci o pobjedama i porazima
        
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


imena = ['Mario', 'Ivan', 'Antea', 'Roko', 'Marina', 'Sabka', 'Stjepan', 'Ana', 'Riki', 'Lucija', 'Mihael', 'Sandro', 'Ivona', 'Emina', 'Sanja', 'Josip']
natjecatelj = []

for i in range (len(imena)): natjecatelj.append(NATJECATELJ(imena[i], 0))

print("-"*40)
print(natjecatelj)

# # meč u kojem je 1 pobijedio 3
# natjecatelj[0].pobjeda
# natjecatelj[1].gubitak

# # meč u kojem je 1 pobijedio 5
# natjecatelj[3].pobjeda
# natjecatelj[2].gubitak

print("-"*40)
print(f'\t\tPob\tGub')
print(f'\t\t-\t-')
for i in range(len(imena)):
    print(f'{natjecatelj[i]}\t\t{natjecatelj[i].vpobjede}\t{natjecatelj[i].vgubitke}')


t1 = TURNIR("glavni", *natjecatelj)

