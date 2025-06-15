
class Natjecatelj ():
    brojnatjecatelja = 0
    
    def __init__ (self, ime, tezina):
        self.ime		= str(ime)
        self.tezina		= int(tezina)
        self.rezultati	= [0, 0]	# podatci o rezultatima
        
        Natjecatelj.brojnatjecatelja += 1
    
    # metode za postavljanje vrijednosti
    def pime (self, tekstimena):
        self.ime = tekstimena
    def ptezina (self, vrijednost):
        self.tezina = vrijednost
    def prezultat (self, *args):
        if args == []:
            self.rezultati = [0, 0]
        else:
            for i in range (2):
                self.rezultati[i] = args[i]
    
    @property
    def pobjeda (self):
        self.rezultati[0] += 1
    @property
    def gubitak (self):
        self.rezultati[1] += 1
    
    # metode za vraćanje podataka
    @property
    def vtezinu (self):
        return self.tezina
    @property
    def vrezultate (self):
        return self.rezultati
    @property
    def vpobjede (self):
        return self.rezultati[0]
    @property
    def vgubitke (self):
        return self.rezultati[1]
    
    def __str__ (self):
        return f'{self.ime}'
    def __repr__ (self):
        return f'#{self.tezina}_{self.ime}'
    
    def __del__ (self):
        Natjecatelj.brojnatjecatelja -= 1


imena = ['Mario', 'Ivan', 'Antea', 'Roko', 'Marina', 'Sabka', 'Stjepan', 'Ana']
natjecatelj = []

for i in range (len(imena)): natjecatelj.append(Natjecatelj(imena[i], 0))

print("-"*40)
print(natjecatelj)
natjecatelj[5].pobjeda
natjecatelj[3].gubitak

print("-"*40)
print(f'\t\tP\tG')
print(f'\t\t-\t-')

for i in range(len(imena)):
    print(f'{natjecatelj[i]}\t\t{natjecatelj[i].vpobjede}\t{natjecatelj[i].vgubitke}')