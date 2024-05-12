#Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)


from szoba import Szoba

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás {self.datum.strftime('%Y-%m-%d')}-ra/-re dátumra a {self.szoba.szobaszam}-as/-es szobára."