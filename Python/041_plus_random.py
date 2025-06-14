from random import randint

# 41 Histogram. Rezultate ispita prikazati u grupama po 10 (0-10,10-20, 20-30,30-40,40-50) te
# prikazati grafički

podatci = []
histogr = []

# varijable za namještanje broja generiranih brojeva ("kolicina") i
# najveće vrijedosti generiranog broja ("raspon")
kolicina = 20
raspon   = 59

# popunjavanje polja nasumičnim brojevima
for i in range (kolicina): podatci.append( randint(0, raspon) )

# sortiranje poja
podatci.sort()

# nađi razred najvećeg podatka da znamo veličinu histograma
razred = podatci[0] // 10
for i in range (1,len(podatci)):
    if podatci[i] // 10 > razred:
        razred = podatci[i] // 10

# popuni histogram početnim vrijednostima
for i in range (razred + 1):
    histogr.append(0)

# izračunaj histogram
for i in range (len(podatci)):
    histogr[ podatci[i] // 10 ] += 1

# ispis podataka
print(f'Za podatke:\t\t{podatci}')
print(f'Histogram sadrži:\t{histogr}')
print("\nGrafički prikaz histograma:\n")


# za potrebe grafikona potrebna je visina histograma, to jest najveći član
najveci = 0         # ova varijabla će čuvati informaciju o najvećem članu
#                       potrebna je zbog ispisivanja visine na histogramu
visina = 0          # ova će se smanjivati u petlji

# petljom pronađi koliko je visok najviši stupac, što
# je u biti najveća vrijednost u polju "histogr"
for i in range (len(histogr)):
    if histogr[i] > najveci:
        najveci = histogr[i]

# za početak su "visina" i "najveci" isti
visina = najveci      

# crtaj historgram u redovima, a njih ima "najveci" komada
for i in range (najveci):
    # prvo ispiši visinu retka, koje idu od "najveci" prema 1
    print(f'{najveci-i}\t ', end="")

    # u petlji prođi sve članove histograma, i ako je neki od njih
    # veći od ili jednak vrijednosti "visina", ispiši crni kvadrat
    # s dva razmaka da se uredno složi sa ispisom polja "histogr",
    # u slučaju da nije, ispiši prazno polje s još dva razmaka
    for j in range (len(histogr)):
        if histogr[j] == visina:
            print("▄  ", end="")    # za vrh stupca koristi "Half block" U+2584
            #                           jer će se spojiti s ostatkom stupca
        elif histogr[j] > visina:
            print("█  ", end="")    # za stupac "Full block" U+2588 zato što
            #                           se on spaja s redovima ispod i iznad
        else:
            print("   ", end="")
        
        # ispiši prazna mjesta u slučaju da se stupac nalazi na
        # vrijednosti koja je višeznamenkasta u histogramu
        dodatak = histogr[j] // 10      # za praćenje znamenki
        while dodatak > 0:
            print(" ", end="")          # dodaj prazno mjesto
            dodatak//=10                # smanji red veličine varijable za praćenje
    
    # nakon što si prošao sve vrijednosti u histogramu, idi u sljedeći redak
    print()
    
    # za sljedeću iteraciju petlje smanji "visina" za jedan
    # kako bi pratio koji redak crtaš
    visina-=1

# iz estetskih razloga ispiši crtu, počni sa crtom ispod brojeva retka
# pa dopiši crtice za svaki član polja "histogr"
# koristi "Box Drawings Light Horizontal" U+2500 kako bi se uredno spojile
print("─"*8, end="")
for i in range (len(histogr)):
    print("─"*3, end="")

    # potrebno je produljiti liniju za svaku
    # višeznamenkastu vrijednost u histogramu
    dodatak = histogr[i] // 10
    while dodatak > 0:
        print("─", end="")
        dodatak//=10

# na kraju uđi u novi red, ispiši i vrijednosti histograma,
# uz "tab" kako bi se uredno poredala s ostatkom grafikona
print(f'\n\t{histogr}')