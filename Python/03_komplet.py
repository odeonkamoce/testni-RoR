# 2 Objekti- student- kreirati klasu student te atribute objekta ime u
# __init__. Nadodati property groupMember= None (ne unosi se u
# konstruktoru ali je definiran u init metodi)
# 2.1 Kreirati repr gdje se ispisuje samo ime
# 2.2 Kreirati metodu setGroupMember koja postavlja kolegu našem objektu
# 2.3 postavljamo uvjet u metdu setGroupMember slučaju da je groupMember već
# postavljen da se ispisuje poruka, imamo partnera

# 3 Zadatak kao prethodni samo da se omogući kreiranje grupe od sve
# skupa tri člana, koristimo listu gdje spremamo ostala dva člana grube
# od zadanog objekta

####### RJEŠENJE ZADATKA 3 ZA GRUPE S PROIZVOLJNIM BROJEM ČLANOVA
####### koje dopušta odvojene grupe, spajanje grupa i uklanjanje članova
####### rj. Mihael Kovač

class Student ():
    
    def __init__ (self, ime):
        self.ime = ime
        self.clangrupe = []
        
        
    # funkcija kojom ću grupirati članove sa instancom self (i međusobno)
    def grupiraj(self, *clanovi):
        
        # za svakog člana kojeg želimo povezati u grupu, potrebno je povezati
        # i sve članove koji su s njim već u grupi; za to ću koristiti popis
        # koji ću napuniti svim članovima svih grupa iz argumenta
        popis_svih_u_grupi = []
        
        # među argumente moramo dodati i self inače bi nam neki njegovi
        # postojeći članovi mogli nedostajati iz ukupnog popisa članova
        c = clanovi + (self,)
        
        # petlja za popunjavanje liste 'popis_svih_u_grupi'
        for element in c:
            if element not in popis_svih_u_grupi:
                popis_svih_u_grupi.append(element)
            for clan in element.clangrupe:
                if clan not in popis_svih_u_grupi:
                    popis_svih_u_grupi.append(clan)
                    
        # s potpunim popisom članova novonastale grupe, pozivam funkciju
        # koja će u rekurziji obaviti povezivanje svih članova
        self.povezivanje(*popis_svih_u_grupi)
        
    
    # rekurzivna funkcija za međusobno povezivanje
    def povezivanje (self, *clanovi):
        for element in clanovi:
            if element is not self:
                if element not in self.clangrupe:
                    self.clangrupe.append(element)
                if self not in element.clangrupe:
                    element.clangrupe.append(self)
            element.povezivanje(*[arg for arg in clanovi if arg is not self])
            
    
    # funkcija kojom će se uklanjati člana iz grupe
    def ukloni (self):
        
        # u svakom članu vlastite grupe potrebno je ukloniti sebe
        for element in self.clangrupe:
            element.clangrupe = [clan for clan in element.clangrupe if clan is not self]
            
        # i nakon toga očistiti vlastitu grupu
        self.clangrupe = []
        
        
    # priprema za ispis
    def __str__ (self):
        
        # za studenta/icu izvan grupe, ispisujem samo ime
        if not self.clangrupe:
            return f'Student/ica {self.ime} nije član grupe.'
        
        # za stuenta/icu u grupi, ispisujem popis članova
        else:
            
            # počinjem s praznim popisom
            popis_clanova = ""
            
            # za svakog člana grupe, dodajem ga u popis
            for element in self.clangrupe:
                popis_clanova += element.ime + ", "
            
            # estetsko micanje zadnjeg ", "
            popis_clanova = popis_clanova [:-2]
            
            #vraćanje potpunog ispisa
            return f'Student/ica {self.ime} je u grupi sa sa {popis_clanova}.'




# --- IZVRŠAVANJE testnog koda


a1 = Student("(1) Mario")
a2 = Student("(2) Elena")
a3 = Student("(3) Adrian")
a4 = Student("(4) Roko")
a5 = Student("(5) Ivana")
a6 = Student("(6) Slavica")
a7 = Student("(7) Goran")
a8 = Student("(8) Filip")

print("-"*20)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

a1.grupiraj(a2, a3, a4)

print("-"*20)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

a5.grupiraj(a7, a8)

print("-"*20)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

a3.ukloni()
a4.ukloni()

print("-"*20)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

a1.grupiraj(a8)

print("-"*20)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)