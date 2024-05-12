#A kód sajnos nem fut le tökéletesen és hibás néhány
#helyen, de megpróbáltam implementálni a lehető leglogikusabb módon az algoritmust.
#A program Visual Studio Code-ban lett megoldva, más prograozási
#környezetben elképzelhető, hogy több hibakódot ír ki.

from datetime import datetime
from szoba import Szoba
from egyagyas import EgyagyasSzoba
from ketagyas import KetagyasSzoba
from foglalas import Foglalas

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.egyagyas = [EgyagyasSzoba("101"), EgyagyasSzoba("202"), EgyagyasSzoba("303")]
        self.ketagyas = [KetagyasSzoba("212"), KetagyasSzoba("323"), KetagyasSzoba("434")]
        self.szobak = self.egyagyas + self.ketagyas
        self.foglalasok = []

    #Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát.
    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and szoba.foglalhato(datum):
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas
        return None

    #Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását.
    def foglalas_lemondasa(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    #Implementálj egy metódust, ami listázza az összes foglalást.
    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(foglalas)

    def szobak_listazasa(self, szobaszam, datum):
            for egyagyas in self.egyagyas:
                print(f"Egyágyas szoba. Szobaszám: {egyagyas.szobaszam}, Ár: {egyagyas.ar} Ft.")
            for ketagyas in self.ketagyas:
                print(f"Kétágyas szoba. Szobaszám: {ketagyas.szobaszam}, Ár: {ketagyas.ar} Ft.")

    #Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. 
    def lefoglalt_szobak(self):
        szalloda = Szalloda("Hotel Ezüstpart")
        szalloda.foglalas("101", datetime(2024, 6, 1))
        szalloda.foglalas("212", datetime(2024, 6, 3))
        szalloda.foglalas("303", datetime(2024, 6, 5))
        szalloda.foglalas("212", datetime(2024, 6, 7))
        szalloda.foglalas("101", datetime(2024, 6, 9))
        self.foglalasok.append = szalloda.foglalas()

#Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás).
while True:
    print("\nVálassz egy műveletet!")
    print("1. Szobák listázása")
    print("2. Foglalás")
    print("3. Foglalás lemondása")
    print("4. Foglalások listázása")
    print("5. Kilépés")

    valasztas = input("Választás: ")

    if valasztas == "1":
        print("Szobák:")
        Szalloda.szobak_listazasa()
    elif valasztas == "2":
        szobaszam = input("Add meg a szobaszámot! ")
        datum_str = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban)! ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        if Szalloda.foglalas(szobaszam, datum) != Szalloda.foglalasok():
            print("Sikeres foglalás!")
        elif Szalloda.foglalas(szobaszam, datum) == Szalloda.foglalasok():
            print("Ez a szoba már le van foglalva!")
        else:
            print("A foglalás nem lehetséges.")
    elif valasztas == "3":
        #Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek
        lemondas_szobaszam = int(input("Melyik szobát szeretnéd lemondani? "))
        lemondas_datum = datetime(input("Melyik dátumra szeretnéd lemondani (ÉÉÉÉ-HH-NN formátumban)? "))
        if lemondas_szobaszam == Szalloda.foglalas(szobaszam) and lemondas_datum == Szalloda.foglalas(datum):
            Szalloda.foglalas_lemondasa
            print("Sikeres lemondás!")
        else:
            print("Még nincs foglalva szoba.")
    elif valasztas == "4":
        print("Foglalások:")
        Szalloda.foglalasok_listazasa()
    elif valasztas == "5":
        print("Köszönjük a látogatást!")
        break
    else:
        print("Érvénytelen választás. Írj be egy számot 1-5 között!")
